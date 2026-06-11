def g(s, p, end):
    if s >= 101:
        return p == end

    if p == end:
        return False

    moves = (s + 2, s * 2)

    return any(g(ns, p + 1, end) for ns in moves)


for s in range(1, 101):
    if g(s, 0, 2):
        print(s)
        break
