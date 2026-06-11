def g(x, y, p, end):
    if x + y >= 105:
        return p in end
    if p == max(end):
        return False
    moves = (
        g(x + 4, y, p + 1, end),
        g(x * 3, y, p + 1, end),
        g(x, y + 4, p + 1, end),
        g(x, y * 3, p + 1, end),
    )
    return any(moves) if (p + 1) % 2 == (end[0] % 2) else all(moves)


for s in range(1, 101):
    if g(4, s, 0, [2]):
        print(s)
        break
