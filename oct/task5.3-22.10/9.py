max_N = 0

for N in range(1, 1000):
    d = []
    n = N
    while n > 0:
        d.append(str(n % 5))
        n //= 5
    if not d:
        d = ["0"]
    s = "".join(d[::-1])

    if N % 10 == 0:
        if len(s) >= 2:
            s += s[-2:]
        else:
            s += s
    else:
        r = (N % 10) * 3
        rd = []
        t = r
        while t > 0:
            rd.append(str(t % 5))
            t //= 5
        if not rd:
            rd = ["0"]
        rs = "".join(rd[::-1])
        s = rs + s

    R = int(s, 5)

    if R < 176 and N > max_N:
        max_N = N

print(max_N)
