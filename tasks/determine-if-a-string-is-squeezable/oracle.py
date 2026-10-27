# Independent reference for "Determine if a string is squeezable" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import re
for s, ch in [('..1111111111111111111111111111111111111111111111111111111111111117777888', '-'), ('..1111111111111111111111111111111111111111111111111111111111111117777888', '7'), ("I never give 'em hell, I just tell the truth, and they think it's hell. ", '.'), ('                                                    --- Harry S Truman  ', ' '), ('                                                    --- Harry S Truman  ', '-'), ('                                                    --- Harry S Truman  ', 'r')]:
    t = re.sub(re.escape(ch) + "+", ch, s)
    print(f"squeeze '{ch}'")
    print(f"<<<{s}>>> length {len(s)}")
    print(f"<<<{t}>>> length {len(t)}")
