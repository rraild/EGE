def g(s, p, end):
    if s >= 71:
        return p == end

    if s < 71 and p == end:
        return 0

    return g(s + 1, p + 1, end) or g(s * 2, p + 1, end)


for s in range(1, 71):
    if g(s, 0, 2):
        print(s)
        break
