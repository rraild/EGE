def g(s, p, end):
    if s >= 128:
        return p == end
    if p == end:
        return 0

    moves = [g(s + 2, p + 1, end), g(s + 5, p + 1, end), g(s * 2, p + 1, end)]

    if p % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 128):
    if g(s, 0, 2):
        print(s)
        break
