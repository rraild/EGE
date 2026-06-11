res = []


def to25(n):
    r = []
    while n > 0:
        r.append(n % 25)
        n = n // 25

    return r[::-1]


mxz = 0
for x in range(1, 2501):
    v = to25(25**150 + 25**100 - x)
    res.append((v.count(0), x))


print(sorted(res, reverse=True))
