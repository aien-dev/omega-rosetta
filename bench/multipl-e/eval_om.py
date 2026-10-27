#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""MultiPL-E evaluator for Omega programs written by humaneval_to_om.py.

Foreign-harness adapter: MultiPL-E calls ``eval_script(path)`` from
``evaluation/src/eval_<ext>.py``, so this file is Python. It is not first-party
Omega and is not part of any Omega product path. Pure standard library.

    OMEGA_OMC=/path/to/omc eval_om.py PROGRAM.om [...]      # one JSON result per line

Compile protocol (pinned omc): ``omc < p.om > p 2> p.err``. Only when omc exits
0 with nothing on stderr is ``p`` made executable and run. The omc file must hash
to OMEGA_OMC_SHA256 (default: the omega-rosetta pin); a mismatch raises before
anything is compiled, so no result is ever recorded against an unpinned compiler.

Outcome -> MultiPL-E ``status`` (``om_status``, ``om_case``):

    omc nonzero / stderr        SyntaxError  compile_error  omc error code
    exit 0 + pass line          OK           pass           -
    exit 0 without pass line    Exception    no_pass_line   -
    exit 1..98                  Exception    wrong_answer   failing test case (exit - 1)
    exit 100..199               Exception    trap           trap code (exit - 100)
    other exit / signal         Exception    exit_other     exit code
    over the time limit         Timeout      timeout        -

MultiPL-E's containerized_eval keeps only status/exit_code/stdout/stderr; the
om_* fields are derivable from exit_code by the table above.
"""

import hashlib
import json
import os
import re
import shlex
import signal
import subprocess
import sys
import tempfile
from pathlib import Path

# Pin of aien-dev/omega-rosetta omega.ref (omega-mv e5b32567a7aff3ce594e3254a622a846a6cd190b).
PINNED_OMC_SHA256 = "2c82480596bbdc50cda9626866209ef662d5834f278f839ff4ce0250c495029f"
# Must equal humaneval_to_om.MPE_OK_LINE: the line main writes after the last case holds.
MPE_OK_LINE = "MultiPL-E Omega: all tests passed"
COMPILE_TIMEOUT = 30
MAX_OUTPUT = 2048
_ERROR_RE = re.compile(r"omc: line (\d+): error (\d+)")
_checked = {}


def omc_path(omc=None) -> str:
    omc = omc or os.environ.get("OMEGA_OMC")
    if not omc:
        raise RuntimeError("eval_om: set OMEGA_OMC to the pinned omc binary")
    return omc


def check_pin(omc: str) -> None:
    """Raise unless the omc file hashes to the pin. Cached by (path, size, mtime)."""
    st = os.stat(omc)
    key = (os.path.realpath(omc), st.st_size, st.st_mtime_ns)
    want = os.environ.get("OMEGA_OMC_SHA256", PINNED_OMC_SHA256)
    if _checked.get(key) == want:
        return
    h = hashlib.sha256()
    with open(omc, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    got = h.hexdigest()
    if got != want:
        raise RuntimeError(f"eval_om: {omc} has sha256 {got}, pin is {want}; refusing to evaluate")
    _checked[key] = want


def _wrap() -> list:
    """Optional command prefix for omc and the program, e.g. 'nice -n 19 taskset -c 10-14'."""
    return shlex.split(os.environ.get("OMEGA_EVAL_WRAP", ""))


def _run(argv, timeout, stdin=None, stdout=subprocess.PIPE):
    """Run argv in its own process group; kill the group on timeout.
    Returns (exit_code or None on timeout, stdout bytes, stderr bytes)."""
    p = subprocess.Popen(
        argv, stdin=stdin or subprocess.DEVNULL, stdout=stdout, stderr=subprocess.PIPE, start_new_session=True
    )
    try:
        out, err = p.communicate(timeout=timeout)
        return p.returncode, out or b"", err or b""
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        out, err = p.communicate()
        return None, out or b"", err or b""


def _text(b: bytes) -> str:
    return b[:MAX_OUTPUT].decode("utf-8", errors="replace")


def eval_script(path: Path, omc=None, timeout=None) -> dict:
    omc = omc_path(omc)
    check_pin(omc)
    if timeout is None:
        timeout = float(os.environ.get("OMEGA_EVAL_TIMEOUT", "15"))
    with tempfile.TemporaryDirectory(prefix="eval_om.") as d:
        exe = os.path.join(d, "p")
        with open(path, "rb") as src, open(exe, "wb") as dst:
            rc, _, err = _run(_wrap() + [omc], COMPILE_TIMEOUT, stdin=src, stdout=dst)
        if rc is None:
            return {"status": "Timeout", "exit_code": -1, "stdout": "", "stderr": "omc timeout",
                    "om_status": "timeout", "om_case": None}
        if rc != 0 or err:
            m = _ERROR_RE.search(err.decode("utf-8", errors="replace"))
            return {"status": "SyntaxError", "exit_code": rc, "stdout": "", "stderr": _text(err),
                    "om_status": "compile_error", "om_case": int(m.group(2)) if m else None}
        os.chmod(exe, 0o755)
        rc, out, err = _run(_wrap() + [exe], timeout)
    result = {"exit_code": rc if rc is not None else -1, "stdout": _text(out), "stderr": _text(err)}
    if rc is None:
        result.update(status="Timeout", om_status="timeout", om_case=None)
    elif rc == 0 and out.endswith((MPE_OK_LINE + "\n").encode()):
        result.update(status="OK", om_status="pass", om_case=None)
    elif rc == 0:
        result.update(status="Exception", om_status="no_pass_line", om_case=None)
    elif 1 <= rc <= 98:
        result.update(status="Exception", om_status="wrong_answer", om_case=rc - 1)
    elif 100 <= rc <= 199:
        result.update(status="Exception", om_status="trap", om_case=rc - 100)
    else:
        result.update(status="Exception", om_status="exit_other", om_case=rc)
    return result


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    for p in argv:
        print(json.dumps({"path": p, **eval_script(Path(p))}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
