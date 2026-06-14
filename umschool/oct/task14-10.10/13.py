for x in range(1, 2070):
    s = 7**230 + 7**130 + 7**30 - x
    res = ""

    while s > 0:
        res += str(s % 7)
        s //= 7

    res = res[::-1]
    if res.count("0") == 199:
        print(x)
