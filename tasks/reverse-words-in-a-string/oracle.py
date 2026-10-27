# Independent reference for "Reverse words in a string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
lines = ['---------- Ice and Fire ------------', '', 'fire, in end will world the say Some', 'ice. in say Some', "desire of tasted I've what From", 'fire. favor who those with hold I', '', '... elided paragraph last ...', '', 'Frost Robert -----------------------']
for line in lines:
    print(" ".join(reversed(line.split())))
