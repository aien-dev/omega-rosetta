# Independent reference for "Elementary cellular automaton" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def run(rule):
    print("rule", rule)
    # the rule table as a dict from neighbourhood strings to the next cell
    table = {f"{k:03b}": "1" if rule >> k & 1 else "0" for k in range(8)}
    cells = "0" * 15 + "1" + "0" * 15
    for _ in range(16):
        print(cells.replace("1", "#").replace("0", "."))
        ring = cells[-1] + cells + cells[0]
        cells = "".join(table[ring[i:i + 3]] for i in range(31))
for t, rule in enumerate((90, 30, 110)):
    if t:
        print()
    run(rule)
