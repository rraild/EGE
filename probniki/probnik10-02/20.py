def g(s, p, end):
    if s >= 46:
        return p == end

    if p == end:
        return 0

    if (p + 1) % 2 == (end % 2):
        return g(s + 2, p + 1, end) or g(s * 2, p + 1, end)
    else:
        return g(s + 2, p + 1, end) and g(s * 2, p + 1, end)


res = []
for s in range(1, 46):
    if g(s, 0, 3) and not g(s, 0, 1):
        res.append(s)

print(min(res), max(res))
