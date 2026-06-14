def g(s, p, end):
    if p == end:
        return s >= 167

    if s >= 167:
        return False

    moves = [s + 9, s * 3]

    if p == 0:
        return any((m < 167) and g(m, p + 1, end) for m in moves)
    else:
        return any(g(m, p + 1, end) for m in moves)


for s in range(1, 131):
    if g(s, 0, 2):
        print(s)
        break
