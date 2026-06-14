def g(s, p, end):
    if s >= 54:
        return p == end
    if p == end:
        return False

    moves = [g(s + 2, p + 1, end), g(s + 3, p + 1, end), g(s * 2, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 54):
    if g(s, 0, 2) and not g(s, 0, 1):
        print(s)
        break
