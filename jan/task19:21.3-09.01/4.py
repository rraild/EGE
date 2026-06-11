def g(s, p, end):
    if s >= 91 and p == end:
        return 1

    if s < 91 and p == end:
        return 0

    if s >= 91 and p != end:
        return 0

    return g(s + 1, p + 1, end) or g(s + 4, p + 1, end) or g(s * 5, p + 1, end)


for s in range(1, 91):
    if g(s, 0, 2):
        print(s)
        break
