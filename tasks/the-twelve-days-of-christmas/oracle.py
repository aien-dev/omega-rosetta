# Independent reference for "The Twelve Days of Christmas" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
gifts = ['A partridge in a pear tree.', 'Two turtle doves,', 'Three french hens,', 'Four calling birds,', 'Five golden rings,', 'Six geese a-laying,', 'Seven swans a-swimming,', 'Eight maids a-milking,', 'Nine ladies dancing,', 'Ten lords a-leaping,', 'Eleven pipers piping,', 'Twelve drummers drumming,']
for d in range(12):
    if d:
        print()
    print(f"On the {days[d]} day of Christmas,")
    print("My true love sent to me:")
    for g in range(d, -1, -1):
        print("And a partridge in a pear tree." if g == 0 and d > 0 else gifts[g])
