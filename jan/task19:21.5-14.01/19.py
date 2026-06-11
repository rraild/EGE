def g(s, p, end):
    if s >= 155:
        return p == end
    if p == end:
        return False
    return g(s + 4, p + 1, end) or g(s * 2, p + 1, end)


for s in range(1, 141):
    if g(s, 0, 2):
        print(s)
        break
