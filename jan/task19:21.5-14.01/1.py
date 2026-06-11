def g(s, p, end):
    if s >= 54:
        return p == end

    if s < 54 and p > end:
        return 0

    return g(s + 1, p + 1, end) or g(s + 2, p + 1, end) or g(s * 3, p + 1, end)


for s in range(1, 54):
    if g(s, 0, 1):
        print(s)
        break
