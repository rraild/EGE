def Del(n, m):
    if n % m == 0:
        return 1
    return 0


e, b = 29_800_000, 12_000_000
for A in range(e, b, -10):
    t = True
    for x in range(e, b, -10):
        f = Del(x, 1422) <= (
            (not (Del(x, A))) <= (not (Del(x, 1900))) or (not (Del(x, 1320)))
        )
        if not f:
            t = False
    if t:
        print(A)
        break
