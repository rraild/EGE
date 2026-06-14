def g(s, p, end):
    if s >= 313:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s + 2, p + 1, end), g(s + 3, p + 1, end), g(s * 3, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


t19 = []
for s in range(1, 313):
    if not g(s, 0, 1) and g(s, 0, 2):
        t19.append(s)
print(sum(t19))

t20 = []
for s in range(1, 313):
    if not g(s, 0, 1) and g(s, 0, 3):
        t20.append(s)
print(min(t20), max(t20))

t21 = []
for s in range(1, 313):
    if not g(s, 0, 2) and g(s, 0, 4):
        t21.append(s)
print(sum(t21))
