# Independent reference for "Determine if a string is collapsible" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools
for s in ["", '"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln ', '..1111111111111111111111111111111111111111111111111111111111111117777888', "I never give 'em hell, I just tell the truth, and they think it's hell. ", '                                                    --- Harry S Truman  ']:
    t = "".join(k for k, _ in itertools.groupby(s))
    print(f"<<<{s}>>> length {len(s)}")
    print(f"<<<{t}>>> length {len(t)}")
