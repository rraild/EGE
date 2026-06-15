def g(s, p, end):
    if s >= 37:
        return p in end

    if p >= max(end):
        return False

    moves = [g(s + 1, p + 1, end), g(s + 4, p + 1, end), g(s * 3, p + 1, end)]

    if ((p + 1) % 2) == (end[0] % 2):
        return any(moves)

    else:
        return all(moves)  # меняем на ANY если "после неудач. хода"


# 19 (а, б)
print([s for s in range(1, 37) if g(s, 0, [1])])
print([s for s in range(1, 37) if g(s, 0, [2])])

# 20
print([s for s in range(1, 37) if g(s, 0, [3])])

# 21
print([s for s in range(1, 37) if g(s, 0, [2, 4]) and not g(s, 0, [2])])
