def g(s, p, end):
    if s >= 128:
        return p == end

    if s < 128 and p > end:
        return 0

    if (p + 1) % 2 == (end % 2):
        return (
            g(s + 2, p + 1, end)
            or g(s + 5, p + 1, end)
            or g(s * 2, p + 1, end)
        )

    else:
        return (
            g(s + 2, p + 1, end)
            and g(s + 5, p + 1, end)
            and g(s * 2, p + 1, end)
        )


for s in range(1, 128):
    if g(s, 0, 3):
        print(s)
