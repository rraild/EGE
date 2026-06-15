def g(x, s, p, end):
    if (x + s) >= 107:
        return p in end

    if p >= max(end):
        return False

    moves = [
        g(x + 1, s, p + 1, end),
        g(x * 2, s, p + 1, end),
        g(x, s + 1, p + 1, end),
        g(x, s * 2, p + 1, end),
    ]

    return any(moves) if (p + 1) % 2 == (end[0] % 2) else all(moves)


x = 13

# print([s for s in range(1, 94) if g(x, s, 0, [2])])
print([s for s in range(1, 94) if g(x, s, 0, [3])])
print([s for s in range(1, 94) if g(x, s, 0, [2, 4]) and not g(x, s, 0, [2])])
