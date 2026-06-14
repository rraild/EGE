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

    if (p + 1) % 2 == end % 2:
        return any(res)
    else:
        return all(res)


for s in range(1, 93):
    if g(10, s, 0, 3) and not g(10, s, 0, 1):
        print(s)
