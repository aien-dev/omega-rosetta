# Independent reference for "Strip comments from a string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import re
for s in ["apples, pears # and bananas", "apples, pears ; and bananas", "  no comment here  "]:
    print("<<<" + re.split("[#;]", s, maxsplit=1)[0].strip(" \t") + ">>>")
