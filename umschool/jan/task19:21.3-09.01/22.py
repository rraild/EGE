def moves(s):
    m = []
    for t in (s + 1, s + 2, s * 2):
        if t % 3 != 0:
            m.append(t)
    return m


def win1(s):
    return any(t >= 154 for t in moves(s))


ans = []
for S in range(1, 153):
    if S % 3 == 0:
        continue
    ok = True
    for p in moves(S):
        if p >= 154:
            ok = False
            break
        if not win1(p):
            ok = False
            break
    if ok:
        ans.append(S)

print(ans)
