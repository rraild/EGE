def moves(s):
    r = [s - 1, s - 2]
    if s % 2 == 0:
        r.append(s // 2)
    return r


def win1(s):
    return any(m < 20 for m in moves(s))


vals = []
for S in range(20, 1000):
    if win1(S):
        continue
    ok = True
    for p in moves(S):
        if p < 20:
            ok = False
            break
        if not win1(p):
            ok = False
            break
    if ok:
        vals.append(S)

print(max(vals))
