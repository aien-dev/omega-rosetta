# Independent reference for "Modular exponentiation" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a = 2988348162058574136915891421498819466320163312926952423791023078876139
b = 2351399303373464486466122544523690094744975233415544072992656881240319
print(f"a^b mod 10^40 = {pow(a, b, 10**40)}")
