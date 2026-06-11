def g(a, b, p, end):
    if a * b > 384:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [
        g(a + 5, b, p + 1, end),
        g(a, b + 5, p + 1, end),
        g(a * 2, b, p + 1, end),
        g(a, b * 2, p + 1, end),
    ]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 385):
    a, b = 8, s
    if not g(a, b, 0, 1):
        if any(
            [
                g(a + 5, b, 1, 2),
                g(a, b + 5, 1, 2),
                g(a * 2, b, 1, 2),
                g(a, b * 2, 1, 2),
            ]  # неудачного хода Пети
        ):
            print(s)
            break

t20 = []
for s in range(1, 385):
    if not g(8, s, 0, 1) and g(8, s, 0, 3):
        t20.append(s)
print(min(t20), max(t20))

t21 = []
for s in range(1, 385):
    if not g(8, s, 0, 2) and g(8, s, 0, 4):
        t21.append(s)
print(min(t21))
