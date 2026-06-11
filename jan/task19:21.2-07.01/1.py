def g(x, s, p, end):
    if (x + s) >= 89 and p == end:
        return 1

    if (x + s) < 89 and p == end:
        return 0

    if (x + s) >= 89 and p != end:
        return 0

    return (
        g(x + 2, s, p + 1, end)
        or g(x * 3, s, p + 1, end)
        or g(x, s + 2, p + 1, end)
        or g(x, s * 3, p + 1, end)
    )


x = 10
for s in range(1, 79):
    if g(x, s, 0, 1):
        print(s)
        break
