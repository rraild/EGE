def g(s, p, end):
    if s >= 56 and p in end:
        return 1

    if s < 56 and p == max(end):
        return 0

    if s >= 56 and p not in end:
        return 0

    if (p + 1) % 2 == (end[0] % 2):
        return g(s + 1, p + 1, end) or g(s * 3, p + 1, end)

    else:
        return g(s + 1, p + 1, end) and g(s * 3, p + 1, end)


for s in range(1, 56):
    if g(s, 0, [2, 4]) and not (g(s, 0, [2])):
        print(s)
