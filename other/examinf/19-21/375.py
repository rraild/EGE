def g(a, b, p, end):
    if a + b >= 212:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(a + b, b, p + 1, end), g(a, a + b, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


t19 = []
for s in range(0, 112):
    if not g(100, s, 0, 1):
        t19.append(s)
print(t19)

t20 = []
for s in range(1, 112):
    if not g(50, s, 0, 1) and g(50, s, 0, 3):
        t20.append(s)
print(t20)  # 37
print(37 + 50)

t21 = []
for s in range(1, 112):
    if not g(10, s, 0, 2) and g(10, s, 0, 4):
        t21.append(s)
print(t21)
