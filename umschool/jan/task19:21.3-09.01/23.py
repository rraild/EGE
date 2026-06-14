from functools import lru_cache


def moves(s):
    r = []
    for t in (s + 1, s + 2, s * 2):
        if t % 3 != 0:
            r.append(t)
    return r


@lru_cache(None)
def game(s):
    if s >= 154:
        return "END"
    ms = moves(s)
    if any(m >= 154 for m in ms):
        return "WIN1"
    if ms and all(game(m) == "WIN1" for m in ms):
        return "LOSS1"
    if any(game(m) == "LOSS1" for m in ms):
        return "WIN2"
    return "OTHER"


ans = []
for S in range(1, 153):
    if S % 3 == 0:
        continue
    if game(S) == "WIN2":
        ans.append(S)

print(f"{ans[0]}{ans[-1]}")
