def g(x, s, p, end, opp="all"):
    if (x + s) >= 66:
        return p in end

    if p == max(end):
        return 0

    moves = [
        g(x + 1, s, p + 1, end, opp),
        g(x * 3, s, p + 1, end, opp),
        g(x, s + 1, p + 1, end, opp),
        g(x, s * 3, p + 1, end, opp),
    ]

    target_parity = end[0] % 2
    next_player_parity = (p + 1) % 2

    if next_player_parity == target_parity:
        return any(moves)

    return all(moves) if opp == "all" else any(moves)


x = 6

ans19 = [s for s in range(1, 60) if g(x, s, 0, [2], opp="any")]
print("19):", min(ans19))

ans20 = [s for s in range(1, 60) if g(x, s, 0, [3]) and not g(x, s, 0, [1])]
print("20):", ans20)

ans21 = [s for s in range(1, 60) if g(x, s, 0, [2, 4]) and not g(x, s, 0, [2])]
print("21):", ans21)
