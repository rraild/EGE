def win1(s):
    return (s - 3 <= 15) or (s - 5 <= 15)


def win2(s):
    for m in (s - 3, s - 5):
        if m <= 15:
            return True
        if win1(m - 3) and win1(m - 5):
            return True
    return False


vals = []
for S in range(16, 47):
    a, b = S - 3, S - 5
    if a <= 15 or b <= 15:
        continue
    if win2(a) and win2(b) and (not win1(a) or not win1(b)):
        vals.append(S)

print(max(vals))
