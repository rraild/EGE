def g(s, p, end):
    if s >= 101:
        return p in end
    if p == max(end):
        return False
    moves = (s + 2, s * 2)
    if (p + 1) % 2 == (end[0] % 2):
        return any(g(ns, p + 1, end) for ns in moves)
    else:
        return all(g(ns, p + 1, end) for ns in moves)


ans = []
for s in range(1, 101):
    if g(s, 0, [3]) and not g(s, 0, [1]):
        ans.append(s)

print(str(min(ans)) + str(max(ans)))
