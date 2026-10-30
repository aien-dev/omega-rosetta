# Independent reference for "Longest common prefix" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import os.path
for s in ['interspecies|interstellar|interstate', 'throne|throne', 'throne|dungeon', 'throne||throne', 'cheese', '', 'prefix|suffix', 'foo|foobar']:
    items = s.split("|") if s else []
    print(f'[{s}] -> "{os.path.commonprefix(items)}"')
