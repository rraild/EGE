def g(x, s, p, end):
    if (x + s) >= 103:
        return p == end

    if p == end:
        return False

    res = [
        g(x + 2, s, p + 1, end),
        g(x, s + 2, p + 1, end),
        g(x + s, s, p + 1, end),
        g(x, s + x, p + 1, end),
    ]

    return any(res)


for s in range(1, 93):
    if g(10, s, 0, 2):
        print(s)
        break
