def g(s, p, end):
    if s <= 12:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s - 1, p + 1, end)]
    if s % 2 == 0:
        moves.append(g(s // 2, p + 1, end))

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


t19 = []
for s in range(13, 100):
    if not g(s, 0, 1) and g(s, 0, 2):
        t19.append(s)
print(max(t19))

t20 = []
for s in range(13, 100):
    if not g(s, 0, 1) and g(s, 0, 3):
        t20.append(s)
print(max(t20))

t21 = []
for s in range(13, 100):
    if not g(s, 0, 2) and g(s, 0, 4):
        t21.append(s)

print(min(t21), max(t21))
