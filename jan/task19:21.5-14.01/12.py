def g(x, s, p, end):
    if (x + s) >= 65:
        return p in end

    if p > max(end):
        return 0

    if (p + 1) % 2 == (end[0] % 2):
        return (
            g(x, s + 2, p + 1, end)
            or g(x, s * 2, p + 1, end)
            or g(x + 2, s, p + 1, end)
            or g(x * 2, s, p + 1, end)
        )

    else:
        return (
            g(x, s + 2, p + 1, end)
            and g(x, s * 2, p + 1, end)
            and g(x + 2, s, p + 1, end)
            and g(x * 2, s, p + 1, end)
        )


x = 3
for s in range(1, 62):
    if g(x, s, 0, [2, 4]) and not g(x, s, 0, [2]):
        print(s)
