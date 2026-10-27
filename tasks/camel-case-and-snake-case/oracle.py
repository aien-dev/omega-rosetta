# Independent reference for "Camel case and snake case" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
SEP = "_- "
def split_edges(s):
    core = s.strip(" ")
    if not core:
        return s, "", ""
    l = len(s) - len(s.lstrip(" "))
    t = len(s.rstrip(" "))
    return s[:l], s[l:t], s[t:]
def snake(s):
    a, core, b = split_edges(s)
    out = []
    for i, c in enumerate(core):
        if c in SEP:
            out.append("_")
        elif "A" <= c <= "Z":
            if i > 0 and core[i - 1] not in SEP:
                out.append("_")
            out.append(c.lower())
        else:
            out.append(c)
    return a + "".join(out) + b
def camel(s):
    a, core, b = split_edges(s)
    out, up = [], False
    for c in core:
        if c in SEP:
            up = True
        else:
            out.append(c.upper() if up and "a" <= c <= "z" else c)
            up = False
    return a + "".join(out) + b
for s in ['snakeCase', 'snake_case', 'variable_10_case', 'variable10Case', 'hurry-up-joe!', 'c://my-docs/happy_Flag-Day/12.doc', '  spaces  ']:
    print(f"{s} -> snake: {snake(s)} -> camel: {camel(s)}")
