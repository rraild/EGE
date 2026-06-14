res = []
for n in range(100, 1000):
    d = [int(x) for x in str(n)]
    s1 = d[0] ** 2 + d[1] ** 2
    s2 = d[1] ** 2 + d[2] ** 2

    v = "".join(map(str, sorted([s1, s2], reverse=True)))

    if v == "5834":
        res.append(n)

print(max(res))
