# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""MultiPL-E translator from the Python benchmarks to Omega (OM-2 profile).

Foreign-harness adapter: MultiPL-E loads translators as Python classes named
``Translator`` in ``dataset_builder/humaneval_to_<ext>.py``, so this file is Python. It
is not first-party Omega and is not part of any Omega product path. Every
program it writes is plain OM-2 for the pinned ``omc`` (see ``bench/README.md`` in
https://github.com/aien-dev/omega-rosetta).

Shape of a translated problem::

    om2
    note <docstring lines>
    note <interface notes: renamed parameters, result-array convention>
    fn NAME PARAM TYPE ... to TYPE
    <completion: body lines and the closing end>
    <tests: one `fn tc_K to bool` per assert, then `fn main to int`>

``main`` returns K+1 when test case K fails (so 1..98), writes the line
``MPE_OK_LINE`` and returns 0 when every case holds. A trap exits 100+code.

Type mapping::

    int        -> long             float     -> f64       bool -> bool
    List[int]  -> view long *      List[float] -> view f64 *
    str        -> view uchar *     (bytes; non-ASCII test strings are refused)
    Tuple[int, int] (homogeneous int/float) -> view long * / view f64 *

A list, string or tuple RESULT becomes an extra last parameter ``res edit T *`` and
the function returns the element count as ``long``; the test checks the count and
then every element. Every other type is refused with a reason (``translate_prompt``
returns None and ``self.refusal`` names why).
"""

import ast
import math
import re
from typing import List, Optional

# omega-mv commit whose pinned omc defines this profile.
OMEGA_MV_PIN = "e5b32567a7aff3ce594e3254a622a846a6cd190b"

# Every word of the pinned omc keyword tables (seed/omc/omc.om `fn kw` and
# `fn kw2` at OMEGA_MV_PIN, decoded from their packed little-endian constants).
# A parameter or function may not use any of these as its name.
KEYWORDS = frozenset(
    """
    abstract accept add and argcnt argread at big bind bitcast bool bound break byte
    chdir chmod chown connect const continue cwd devcall devctl div dupfd edit else
    end envcnt envread eq execprog exit export f32 f64 fabs faccess false fchdir
    fchmod fclose fdsync field flock fmax fmin fn fopen for fork free fresh fseek
    fsqrt fstat fsync ftrunc ge get getdnts getegid geteuid getgid getpgid getpid
    getppid getsid getuid global gt holds i16 i32 i64 i8 if inline int killpid
    layout le len link listen little long lstat lt makedir mapaddr mapbind mapdrop
    mapget maphold mapnew mapread mapset mapwrite memfd monons mul ne neg new not
    note offsetof open ops or out own part peercred pipefds pollfds pread put pwrite
    random read readlnk realns recv rem renames ret rmdir rotl rotr seal send
    sendmsg setpgid setsid shl short shr shutdown sizeof sleepns sockname socknew
    sockopt stat struct sub symlnk syncfs text to trap true truncate u16 u32 u64 u8
    uchar uint ulong umask unlink unroll ushort uvmctl view void waitio waitpid
    while write xor
    """.split()
)
# Names the generated test harness itself declares.
HARNESS_NAMES = frozenset(["main", "res", "r", "w", "mpe_ok", "om2", "ir"])
HARNESS_NAME_RE = re.compile(r"(tc_\d+|t\d+_\d+|a\d+)\Z")

MAX_LOCAL = 8  # error 13: a non-function name has at most 8 characters
MAX_FN = 63  # function names
MAX_SLOTS = 6  # error 9: six parameter slots; an unsized view takes two
MAX_CASES = 98  # exit codes 1..98 name the failing case; 100+ are traps
RESULT_CAP = 4096  # minimum capacity of the result array handed to the candidate
I64_MIN, I64_MAX = -(2**63), 2**63 - 1
MPE_OK_LINE = "MultiPL-E Omega: all tests passed"


class Refused(Exception):
    """A problem the OM-2 mapping cannot express. ``code`` is the tally key."""

    def __init__(self, code: str, detail: str = ""):
        super().__init__(f"{code}: {detail}" if detail else code)
        self.code = code
        self.detail = detail


class Scalar:
    def __init__(self, om: str):
        self.om = om  # long | f64 | bool

    slots = 1

    def __repr__(self):
        return self.om


class Seq:
    """A list, string or fixed tuple: an unsized view of `elem`."""

    def __init__(self, elem: str, py: str, fixed: Optional[int] = None):
        self.elem = elem  # long | f64 | uchar
        self.py = py  # list | str | tuple
        self.fixed = fixed

    slots = 2

    def __repr__(self):
        return f"view {self.elem} *"


SCALARS = {"int": "long", "float": "f64", "bool": "bool"}
SEQ_ELEMS = {"int": "long", "float": "f64"}


def _head(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return type(node).__name__


def om_type(ann: Optional[ast.expr]):
    """Map one Python annotation to Scalar/Seq, or raise Refused."""
    if ann is None:
        raise Refused("type:untyped", "parameter or return has no annotation")
    text = ast.unparse(ann)
    if isinstance(ann, ast.Constant) and ann.value is None:
        raise Refused("type:None", "no result value to test")
    if isinstance(ann, ast.Name):
        if ann.id in SCALARS:
            return Scalar(SCALARS[ann.id])
        if ann.id == "str":
            return Seq("uchar", "str")
        raise Refused(f"type:{ann.id}", text)
    if isinstance(ann, ast.Subscript):
        head = _head(ann.value)
        if head in ("List", "list"):
            inner = ann.slice
            if isinstance(inner, ast.Name) and inner.id in SEQ_ELEMS:
                return Seq(SEQ_ELEMS[inner.id], "list")
            if isinstance(inner, ast.Name) and inner.id == "str":
                raise Refused("type:List[str]", "OM-2 has no array-of-strings type")
            if isinstance(inner, ast.Name) and inner.id == "bool":
                raise Refused("type:List[bool]", "omc refuses bool arrays (new bool N, error 9)")
            raise Refused("type:List[compound]", text)
        if head in ("Tuple", "tuple"):
            elts = ann.slice.elts if isinstance(ann.slice, ast.Tuple) else [ann.slice]
            names = [e.id if isinstance(e, ast.Name) else None for e in elts]
            if len(set(names)) == 1 and names[0] in SEQ_ELEMS:
                return Seq(SEQ_ELEMS[names[0]], "tuple", fixed=len(elts))
            raise Refused("type:Tuple[mixed]", text)
        raise Refused(f"type:{head}", text)
    raise Refused("type:other", text)


def _name_ok(name: str, used: set) -> bool:
    return (
        name not in KEYWORDS
        # The pinned omc looks a word up in its keyword table by its first eight bytes
        # only (omc.om `fn kw` takes one packed ulong), so it reads a longer name such as
        # truncate_number or continue_x as the keyword truncate / continue (error 16).
        and name[:8] not in KEYWORDS
        and name not in HARNESS_NAMES
        and name not in used
        and not HARNESS_NAME_RE.match(name)
    )


def fit_name(py: str, used: set, limit: int) -> str:
    """An Omega name for Python identifier `py`: at most `limit` characters, not a
    keyword (nor starting with an eight-letter one), not a harness name, not used."""
    base = py[:limit]
    if len(base) > 8 and base[:8] in KEYWORDS:
        base = base[0].upper() + base[1:]
    if _name_ok(base, used):
        return base
    for k in range(1, 100):
        suffix = "_" if k == 1 else f"_{k}"
        cand = base[: limit - len(suffix)] + suffix
        if _name_ok(cand, used):
            return cand
    raise Refused("name:unmappable", py)


def f64_literal(v) -> str:
    """Exact round-trip OM-2 float literal (digits.digits[e[-]digits])."""
    f = float(v)
    if not math.isfinite(f):
        raise Refused("value:non-finite float", repr(v))
    if isinstance(v, int) and float(f) != v:
        raise Refused("value:int not exact in f64", repr(v))
    r = repr(f)
    if "e" in r:
        mant, exp = r.split("e")
        if "." not in mant:
            mant += ".0"
        return f"{mant}e{int(exp)}"
    if "." not in r:
        r += ".0"
    return r


class OmExpr(str):
    """A rendered expression (for doctests and the seen_tests table) that keeps
    its structure in `.node` for test generation."""

    def __new__(cls, text: str, node):
        s = super().__new__(cls, text)
        s.node = node
        return s


def _render(node) -> str:
    kind = node[0]
    if kind == "lit":
        v = node[1]
        if isinstance(v, bool):
            return "true" if v else "false"
        if isinstance(v, float):
            return repr(v)
        if isinstance(v, str):
            return '"' + v.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t") + '"'
        if v is None:
            return "none"
        return str(v)
    if kind == "var":
        return node[1]
    if kind in ("list", "tuple", "set"):
        o, c = {"list": "[]", "tuple": "()", "set": "{}"}[kind]
        return o + ", ".join(_render(e) for e in node[1]) + c
    if kind == "dict":
        return "{" + ", ".join(f"{_render(k)}: {_render(v)}" for k, v in zip(node[1], node[2])) + "}"
    if kind == "call":
        parts = [_render(node[1])] + [_render(a) for a in node[2]]
        return " ".join(parts)
    raise ValueError(node)


_TEXT_SAFE = re.compile(rb"[\x20-\x7e\n\t]*\Z")


def _text_literal(b: bytes) -> Optional[str]:
    """An OM-2 `text` literal for bytes b, or None when b needs an escape omc lacks."""
    if not _TEXT_SAFE.match(b):
        return None
    s = b.decode("ascii")
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t") + '"'


class Translator:
    stop = ["\nfn ", "\nstruct ", "\nglobal ", "\ntext ", "\nconst ", "\nlayout ", "\nabstract "]

    def __init__(self):
        self.refusal: Optional[Refused] = None
        self.params = []  # [(py_name, om_name, type)]
        self.ret = None
        self.fn = None
        self.py_fn = None
        self.res = None
        self.cases = []

    def file_ext(self):
        return "om"

    def no_completion_prompt_stub(self):
        return "trap 14\nend\n"

    # ---- prompt ---------------------------------------------------------------

    def translate_prompt(self, name: str, args: List[ast.arg], returns, description: str) -> Optional[str]:
        self.refusal = None
        try:
            return self._prompt(name, args, returns, description)
        except Refused as e:
            self.refusal = e
            return None

    def _prompt(self, name, args, returns, description):
        self.py_fn = name
        self.fn = fit_name(name, set(), MAX_FN)
        used = {self.fn}
        self.params = []
        for a in args:
            t = om_type(a.annotation)
            om = fit_name(a.arg, used, MAX_LOCAL)
            used.add(om)
            self.params.append((a.arg, om, t))
        self.ret = om_type(returns)
        self.res = None
        if isinstance(self.ret, Seq):
            self.res = "res"  # HARNESS_NAMES keeps parameters off this name
        slots = sum(t.slots for _, _, t in self.params) + (2 if self.res else 0)
        if slots > MAX_SLOTS:
            raise Refused("abi:parameter slots", f"{slots} > {MAX_SLOTS}")

        lines = ["om2"]
        for line in description.strip().split("\n"):
            lines.append(("note " + line).rstrip())
        renamed = [(py, om) for py, om, _ in self.params if py != om]
        if self.fn != name:
            renamed.insert(0, (name, self.fn))
        for py, om in renamed:
            lines.append(f"note Omega name: {py} is {om} here.")
        if self.res:
            what = {"str": "bytes", "list": "elements", "tuple": "elements"}[self.ret.py]
            lines.append(
                f"note Result: write the {what} into res (len res >= {RESULT_CAP}) and return how many were written."
            )
        sig = [self.fn]
        for _, om, t in self.params:
            sig.append(f"{om} {t.om}" if isinstance(t, Scalar) else f"{om} view {t.elem} *")
        if self.res:
            sig.append(f"res edit {self.ret.elem} *")
        rt = "long" if self.res else self.ret.om
        lines.append("fn " + " ".join(sig) + f" to {rt}")
        return "\n".join(lines) + "\n"

    # ---- values ---------------------------------------------------------------

    def gen_literal(self, c):
        return ("lit", c)

    def gen_var(self, v):
        if v == "candidate" or v == self.py_fn:
            return ("var", self.fn or v)
        return ("var", v)

    def gen_list(self, l):
        return ("list", l)

    def gen_tuple(self, t):
        return ("tuple", t)

    def gen_dict(self, keys, values):
        return ("dict", keys, values)

    def gen_set(self, s):
        return ("set", s)

    def gen_call(self, func, args):
        return ("call", func, args)

    def finalize(self, expr, context):
        return OmExpr(_render(expr), expr)

    # ---- tests ----------------------------------------------------------------

    def test_suite_prefix_lines(self, entry_point):
        self.cases = []
        return []

    def test_suite_suffix_lines(self):
        lines = [f'text mpe_ok "{MPE_OK_LINE}\\n"', "fn main to int"]
        for k in range(len(self.cases)):
            lines += [f"if not tc_{k}", f"ret {k + 1}", "end"]
        lines += ["w = write 1 mpe_ok 0 len mpe_ok", "ret 0", "end"]
        return lines

    def _scalar(self, node, t: Scalar, rhs: bool) -> str:
        if node[0] != "lit":
            raise Refused("value:non-literal", _render(node))
        v = node[1]
        if t.om == "bool":
            if isinstance(v, bool):
                return "true" if v else "false"
            if rhs and isinstance(v, int) and v in (0, 1):
                return "true" if v else "false"
            raise Refused("value:not a bool", repr(v))
        if t.om == "long":
            if isinstance(v, bool):
                return "1" if v else "0"
            if isinstance(v, float) and v.is_integer():
                v = int(v)
            if not isinstance(v, int):
                raise Refused("value:not an int", repr(v))
            if not I64_MIN <= v <= I64_MAX:
                raise Refused("value:int outside i64", repr(v))
            return str(v)
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise Refused("value:not a float", repr(v))
        return f64_literal(v)

    def _elements(self, node, t: Seq, rhs: bool) -> List[str]:
        if t.py == "str":
            if node[0] != "lit" or not isinstance(node[1], str):
                raise Refused("value:not a str", _render(node))
            if not node[1].isascii():
                raise Refused("value:non-ASCII string", "Omega strings are bytes, Python str is code points")
            return [str(b) for b in node[1].encode("ascii")]
        if node[0] not in ("list", "tuple"):
            raise Refused("value:not a sequence", _render(node))
        if t.fixed is not None and len(node[1]) != t.fixed:
            raise Refused("value:tuple arity", _render(node))
        return [self._scalar(e, Scalar(t.elem), rhs) for e in node[1]]

    def deep_equality(self, left, right):
        try:
            return self._case(left.node, right.node)
        except Refused as e:
            self.refusal = e
            raise

    def _case(self, call, expect):
        if call[0] != "call" or call[1] != ("var", self.fn):
            raise Refused("tests:not a direct candidate call", _render(call))
        if len(call[2]) != len(self.params):
            raise Refused("tests:arity", _render(call))
        k = len(self.cases)
        if k >= MAX_CASES:
            raise Refused("tests:too many cases", f"> {MAX_CASES}")
        texts, body, argv = [], [], []
        for j, (node, (_, _, t)) in enumerate(zip(call[2], self.params)):
            if isinstance(t, Scalar):
                argv.append(self._scalar(node, t, rhs=False))
                continue
            elems = self._elements(node, t, rhs=False)
            # An empty string goes through `part a 0 0`, never `text t ""`: the pinned omc
            # takes a zero-length name as an unsized parameter (omc.om arrarg, nm_len 0)
            # and passes a stale register as the count, so `len` is garbage in the callee.
            if t.py == "str" and elems:
                lit = _text_literal(node[1].encode("ascii"))
                if lit is not None:
                    texts.append(f"text t{k}_{j} {lit}")
                    argv.append(f"t{k}_{j}")
                    continue
            zero = "0.0" if t.elem == "f64" else "0"
            body.append(f"a{j} = new {t.elem} {max(1, len(elems))} {zero}")
            body += [f"put a{j} {i} {v}" for i, v in enumerate(elems)]
            argv.append(f"a{j}" if elems else f"part a{j} 0 0")
        if self.res:
            zero = "0.0" if self.ret.elem == "f64" else "0"
            exp = self._elements(expect, self.ret, rhs=True)
            body.append(f"res = new {self.ret.elem} {max(RESULT_CAP, len(exp))} {zero}")
            argv.append("res")
            body.append(f"r = {self.fn} {' '.join(argv)}".rstrip())
            body += [f"if ne r {len(exp)}", "ret false", "end"]
            for i, v in enumerate(exp):
                body += [f"if ne get res {i} {v}", "ret false", "end"]
            body.append("ret true")
        else:
            exp = self._scalar(expect, self.ret, rhs=True)
            body.append(f"r = {self.fn} {' '.join(argv)}".rstrip())
            body.append(f"ret eq r {exp}")
        self.cases.append(k)
        return "\n".join(texts + [f"fn tc_{k} to bool"] + body + ["end"])
