def g(s, p, end):
    if s >= 46:
        return p in end

    if p > max(end):
        return 0

    if (p + 1) % 2 == (end[0] % 2):
        return g(s + 2, p + 1, end) or g(s * 2, p + 1, end)
    else:
        return g(s + 2, p + 1, end) and g(s * 2, p + 1, end)


for s in range(1, 46):
    if g(s, 0, [2, 4]) and not g(s, 0, [2]):
        print(s)
        break
