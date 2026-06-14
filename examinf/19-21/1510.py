def g(s, p, end):
    if s <= 73:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s - 2, p + 1, end), g(s - 4, p + 1, end), g(s // 2, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(74, 300):
    if not g(s, 0, 1) and g(s, 0, 2):
        print(s)
        break

for s in range(74, 300):
    if not g(s, 0, 1) and g(s, 0, 3):
        print(s)

for s in range(74, 300):
    if not g(s, 0, 2) and g(s, 0, 4):
        print(s)
        break
