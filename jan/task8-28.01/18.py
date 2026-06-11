v, n = 4, 10
res = 0

for start in range(8):
    word = [None] * 14
    word[start : start + 7] = "ПЛЕНДИР"

    if any(
        i in [0, 1, 12, 13] and word[i] and word[i] not in "ЕИУЯ"
        for i in range(14)
    ):
        continue

    p = 1
    for i in range(14):
        if word[i] is None:
            p *= v if i in [0, 1, 12, 13] else n
    res += p

print(res)
