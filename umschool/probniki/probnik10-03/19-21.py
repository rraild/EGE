def g(s, p, end):
    if s >= 88:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s + 2, p + 1, end), g(s * 2 - 1, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


res19 = []
for s in range(1, 88):
    m1 = s + 2
    m2 = s * 2 - 1

    v_win_after_m1 = (m1 < 88) and (m1 + 2 >= 88 or m1 * 2 - 1 >= 88)
    v_win_after_m2 = (m2 < 88) and (m2 + 2 >= 88 or m2 * 2 - 1 >= 88)

    if v_win_after_m1 or v_win_after_m2:
        res19.append(s)

print(min(res19))

res20 = []
for s in range(1, 88):
    if not g(s, 0, 1) and g(s, 0, 3):
        res20.append(s)
print(*res20)

for s in range(1, 88):
    if not g(s, 0, 2) and g(s, 0, 4):
        print(s)
        break
