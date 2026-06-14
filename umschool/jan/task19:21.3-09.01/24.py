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
    if ms and all(game(m) in ("WIN1", "WIN2") for m in ms):
        return "LOSS12"
    return "OTHER"


ans = []
for S in range(1, 153):
    if S % 3 == 0:
        continue
    ms = moves(S)
    if not ms:
        continue
    if all(game(m) in ("WIN1", "WIN2") for m in ms) and any(
        game(m) != "WIN1" for m in ms
    ):
        ans.append(S)

print(max(ans))
