def h(a):
    return (a + 1) // 2


def g(x, y, p, end):
    if x + y <= 22:
        return p in end
    if p == max(end):
        return False
    moves = (
        g(x - 1, y, p + 1, end),
        g(h(x), y, p + 1, end),
        g(x, y - 1, p + 1, end),
        g(x, h(y), p + 1, end),
    )
    return any(moves) if (p + 1) % 2 == (end[0] % 2) else all(moves)


for s in range(13, 500):
    if g(10, s, 0, [2, 4]) and not g(10, s, 0, [2]):
        print(s)
        break
