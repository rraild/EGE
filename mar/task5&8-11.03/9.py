r = []
for k in range(1000, 10000):
    d = [int(x) for x in str(k)]
    s = sum(d)
    m = max(d)
    n = min(d)

    p1 = s - m
    p2 = s - n

    l = "".join(map(str, sorted([p1, p2], reverse=True)))

    if l == "2011":
        r.append(k)

print(min(r))
