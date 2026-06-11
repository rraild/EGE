def g(s, ls_move, p, end):
    if s >= 34:
        return p % 2 == end % 2

    moves = []
    if ls_move != 1:
        moves.append(g(s + 1, 1, p + 1, end))
    if ls_move != 2:
        moves.append(g(s + 2, 2, p + 1, end))
    if ls_move != 3:
        moves.append(g(s * 2, 3, p + 1, end))

    if (p + 1) % 2 == end % 2:
        return any(moves)

    return all(moves)


# 19
# for s in range(1, 34):
#     if g(s, 0, 0, 2):
#         print(s)

# 20 руками
# for s in range(1, 34):
#     if g(s, 0, 0, 3) and not g(s, 0, 0, 1):
#         print(s)

# 21
# for s in range(1, 34):
#     if g(s, 0, 0, 4) and not g(s, 0, 0, 2):
#         print(s)
