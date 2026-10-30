# Independent reference for "Count the coins" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: {SeriesCoefficient[1/((1-x)(1-x^5)(1-x^10)(1-x^25)),{x,0,100}],
# (the same count to 100000 with 50 and 100 added)} -> {242, 13398445413854501}
# Counted without the change-making table. 1-cent coins fill any remainder, so the ways to make s from
# 1, 5, 10 are the pairs (n5, n10) with 5*n5 + 10*n10 <= s: with t = s // 5 and h = t // 2 that is
# sum over j = 0..h of (t - 2j + 1) = (h + 1)(t + 1) - h(h + 1). 25s are enumerated on top of that.
# 50s and 100s together make 50*m cents in m // 2 + 1 ways (n100 = 0..m//2), so m is enumerated last.
def ways_1_5_10(s):
    t = s // 5
    h = t // 2
    return (h + 1) * (t + 1) - h * (h + 1)
def ways_to_25(s):
    return sum(ways_1_5_10(s - 25 * k) for k in range(s // 25 + 1))
def ways_to_100(s):
    return sum((m // 2 + 1) * ways_to_25(s - 50 * m) for m in range(s // 50 + 1))
print("ways to make 100 cents from 1, 5, 10, 25:", ways_to_25(100))
print("ways to make 100000 cents from 1, 5, 10, 25, 50, 100:", ways_to_100(100000))
