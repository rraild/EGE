def moves(s, last):
    r = []
    if last != 1:
        r.append((s + 1, 1))
    if last != 2:
        r.append((s + 2, 2))
    if last != 3:
        r.append((s * 2, 3))
    return r


def win1(s, last):
    return any(ns >= 43 for ns, _ in moves(s, last))


ans = []
for S in range(1, 43):
    if win1(S, 0):
        continue
    ok = True
    for p, lastp in moves(S, 0):
        if p >= 43:
            ok = False
            break
        if not win1(p, lastp):
            ok = False
            break
    if ok:
        ans.append(S)

print(ans)
