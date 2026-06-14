def g(s, p, end):
    if s >= 39:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s + 1, p + 1, end), g(s + 3, p + 1, end), g(s * 2, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 39):
    if g(s, 0, 2):
        print(s)
        break

for s in range(1, 39):
    if not g(s, 0, 1) and g(s, 0, 3):
        print(s)

for s in range(1, 39):
    if not g(s, 0, 2) and g(s, 0, 4):
        print(s)
        break
