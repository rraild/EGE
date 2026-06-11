def g(x, s, p, end):
    if (x + s) >= 65:
        return p == end

    if p > end:
        return 0

    return (
        g(x, s + 1, p + 1, end)
        or g(x, s * 2, p + 1, end)
        or g(x + 1, s, p + 1, end)
        or g(x * 2, s, p + 1, end)
    )


x = 3
for s in range(1, 62):
    if g(x, s, 0, 1):
        print(s)
        break
