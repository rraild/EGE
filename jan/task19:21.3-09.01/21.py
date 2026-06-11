from functools import lru_cache


def moves(s):
    m = [s - 1, s - 2]
    if s % 2 == 0:
        m.append(s // 2)
    return m


@lru_cache(None)
def game(s):
    if any(x < 20 for x in moves(s)):
        return "WIN1"
    if all(game(x) == "WIN1" for x in moves(s)):
        return "LOSS1"
    if any(game(x) == "LOSS1" for x in moves(s)):
        return "WIN2"
    if all(game(x) in ("WIN1", "WIN2") for x in moves(s)):
        return "LOSS12"
    return "OTHER"


s21 = []
for s in range(20, 100):
    if game(s) == "LOSS12":
        s21.append(s)

print(s21)
