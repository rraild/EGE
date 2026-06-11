def g(s, p, end):
    if s >= 46:
        return p in end
    if p == max(end):
        return False
    moves = (g(s + 2, p + 1, end), g(s * 2, p + 1, end))
    return any(moves) if (p + 1) % 2 == (end[0] % 2) else all(moves)


ans = [s for s in range(1, 46) if g(s, 0, [2])]
print(ans)
