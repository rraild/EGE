for x in range(1, 5030 + 1):
    s = 6**260 + 6**160 + 6**60 - x
    res = ""

    while s > 0:
        res += str(s % 6)
        s //= 6

    res = res[::-1]
    if res.count("2") == res.count("3"):
        print(x)
