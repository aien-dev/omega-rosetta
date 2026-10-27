# Independent reference for "Leap year" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import calendar
for y in [1900, 1996, 2000, 2023, 2024, 2100, 2400]:
    print(f"{y} is {'a' if calendar.isleap(y) else 'not a'} leap year")
