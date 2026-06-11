r = []
for n in range(100, 1000):
    d = [int(x) for x in str(n)]
    p = d[0] * d[1] * d[2]
    s = sum(d)

    v = "".join(map(str, sorted([p, s], reverse=True)))

    if v == "6012":
        r.append(n)

print(max(r))
