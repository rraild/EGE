res = []
for k in range(1000, 10000):
    d = [int(x) for x in str(k)]
    s = sum(d)
    m, n = max(d), min(d)

    p1 = s - m
    p2 = s - n

    l = "".join(map(str, sorted([p1, p2])))

    if l == "1318":
        res.append(k)

print(min(res))
