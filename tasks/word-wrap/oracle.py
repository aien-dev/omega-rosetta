# Independent reference for "Word wrap" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import textwrap
para = "In olden times when wishing still helped one, there lived a king whose daughters were all beautiful, but the youngest was so beautiful that the sun itself, which has seen so much, was astonished whenever it shone in her face. Close by the king's castle lay a great dark forest, and under an old lime-tree in the forest was a well, and when the day was very warm, the king's child went out into the forest and sat down by the side of the cool fountain, and when she was bored she took a golden ball, and threw it up on high and caught it, and this ball was her favorite plaything."
print("\n".join(textwrap.wrap(para, 72, break_on_hyphens=False, break_long_words=False)))
print("----")
print("\n".join(textwrap.wrap(para, 40, break_on_hyphens=False, break_long_words=False)))
