from functools import lru_cache


def moves(s, last):
    res = []
    if last != 1:
        res.append((s + 1, 1))
    if last != 2:
        res.append((s + 2, 2))
    if last != 3:
        res.append((s * 2, 3))
    return res


@lru_cache(None)
def win1(s, last):
    return any(ns >= 43 for ns, _ in moves(s, last))


@lru_cache(None)
def loss1(s, last):
    ms = moves(s, last)
    return (not win1(s, last)) and all(win1(ns, nl) for ns, nl in ms)


@lru_cache(None)
def win2(s, last):
    return (not win1(s, last)) and any(
        loss1(ns, nl) for ns, nl in moves(s, last)
    )


ans = []
for S in range(1, 43):
    ms = moves(S, 0)
    if all((win1(ns, nl) or win2(ns, nl)) for ns, nl in ms) and any(
        not win1(ns, nl) for ns, nl in ms
    ):
        ans.append(S)

print(ans)
