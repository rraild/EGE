from functools import lru_cache


def moves(s):
    m = [s - 1, s - 2]
    if s % 2 == 0:
        m.append(s // 2)
    return m


@lru_cache(None)
def game(s):
    if any(n < 20 for n in moves(s)):
        return "WIN1"

    if all(game(n) == "WIN1" for n in moves(s)):
        return "LOSS1"

    if any(game(n) == "LOSS1" for n in moves(s)):
        return "WIN2"

    return "OTHER"


s20 = []
for s in range(20, 100):
    if game(s) == "WIN2":
        s20.append(s)

print(s20)
