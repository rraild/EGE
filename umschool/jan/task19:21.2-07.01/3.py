def g(x, s, p, end):
    if (x + s) >= 89 and p in end:
        return 1

    if (x + s) < 89 and p == max(end):
        return 0

    if (x + s) >= 89 and p not in end:
        return 0

    if (p + 1) % 2 == end[0] % 2:
        return (
            g(x + 2, s, p + 1, end)
            or g(x * 3, s, p + 1, end)
            or g(x, s + 2, p + 1, end)
            or g(x, s * 3, p + 1, end)
        )

    else:
        return (
            g(x + 2, s, p + 1, end)
            and g(x * 3, s, p + 1, end)
            and g(x, s + 2, p + 1, end)
            and g(x, s * 3, p + 1, end)
        )


x = 10
for s in range(1, 79):
    if g(x, s, 0, [2, 4]) and not (g(x, s, 0, [2])):
        print(s)
