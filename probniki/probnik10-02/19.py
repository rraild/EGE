def g(s, p):
    if s >= 46:
        return p == 2

    if p == 2:
        return 0

    if p % 2 == 0:
        return g(s + 2, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 2, p + 1) or g(s * 2, p + 1)


for s in range(1, 46):
    if g(s, 0):
        print(s)
        break
