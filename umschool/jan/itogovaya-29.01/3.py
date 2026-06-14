def g(s, p, end):
    if s >= 54:
        return p % 2 == end % 2
    if p == end:
        return False

    moves = [s + 2, s + 3, s * 2]
    res = [g(m, p + 1, end) for m in moves]

    if (p + 1) % 2 == end % 2:
        return any(res)
    else:
        return all(res)


ans = []
for s in range(1, 54):
    if g(s, 0, 4) and not g(s, 0, 2):
        ans.append(s)

print(ans)
