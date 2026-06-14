def g(a, b, p, end):
    if a + b <= 60:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [
        g(a - 5, b, p + 1, end),
        g(a, b - 3, p + 1, end),
        g(a // 2, b, p + 1, end),
        g(a, (b + 1) // 2, p + 1, end),
    ]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(5, 151):
    a = 130
    petya_moves = [(a - 5, s), (a, s - 3), (a // 2, s), (a, (s + 1) // 2)]

    if any(g(m[0], m[1], 1, 2) for m in petya_moves):
        print(s)

print("------------------------------------------------")
for s in range(5, 151):
    if not g(130, s, 0, 1) and g(130, s, 0, 3):
        print(s)

print("------------------------------------------------")
for s in range(5, 151):
    if not g(130, s, 0, 3) and g(130, s, 0, 5):
        print(s)
print(34 * 35 * 36 * 61 * 62)
