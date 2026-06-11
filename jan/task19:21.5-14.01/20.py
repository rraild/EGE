def g(s, p, end):
    if s >= 155:
        return p in end
    if p == max(end):
        return False
    moves = (g(s + 4, p + 1, end), g(s * 2, p + 1, end))
    return any(moves) if (p + 1) % 2 == (end[0] % 2) else all(moves)


ans = [s for s in range(1, 141) if g(s, 0, [3]) and not g(s, 0, [1])]
print(str(min(ans)) + str(max(ans)))
