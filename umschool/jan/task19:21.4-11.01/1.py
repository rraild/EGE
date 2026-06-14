def g(x, s, p, end, win_sum, opp="all"):
    if (x + s) >= win_sum:
        return p in end

    if p == max(end):
        return 0

    moves = [
        g(x + 1, s, p + 1, end, win_sum, opp),
        g(x * 3, s, p + 1, end, win_sum, opp),
        g(x, s + 1, p + 1, end, win_sum, opp),
        g(x, s * 3, p + 1, end, win_sum, opp),
    ]

    target_parity = end[0] % 2
    next_player_parity = (p + 1) % 2

    if next_player_parity == target_parity:
        return any(moves)

    return all(moves) if opp == "all" else any(moves)


x0 = 3
WIN = 80

ans19 = [S for S in range(1, 77) if g(x0, S, 0, [2], WIN, opp="any")]
print("19):", ans19)


ans20 = [
    S
    for S in range(1, 77)
    if g(x0, S, 0, [3], WIN) and not g(x0, S, 0, [1], WIN)
]
print("20):", ans20)

ans21 = [
    S
    for S in range(1, 77)
    if g(x0, S, 0, [2, 4], WIN) and not g(x0, S, 0, [2], WIN)
]
print("21):", ans21)
