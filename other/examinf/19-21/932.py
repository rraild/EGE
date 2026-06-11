def g(s, p):
    if s >= 82:
        return p
    if p > 4:
        return 0

    moves = [g(s + 2, p + 1), g(s + 4, p + 1), g(s * 3, p + 1)]

    if (p + 1) % 2 != 0:
        res = [m for m in moves if m > 0]
        return min(res) if res else 0
    else:
        if all(m > 0 for m in moves):
            return max(moves)
        else:
            return 0


for s in range(1, 82):
    if (s + 2) * 3 >= 82 or (s + 4) * 3 >= 82 or (s * 3) * 3 >= 82:
        if s * 3 < 82:
            print(s)
            break

print("----")
for s in range(1, 82):
    if g(s, 0) == 3:
        print(s)

print("----")
ans_21 = []
for s in range(1, 82):
    if g(s, 0) == 2 or g(s, 0) == 4:
        ans_21.append(s)
if ans_21:
    print(max(ans_21))