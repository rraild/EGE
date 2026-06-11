max_N = 0

for N in range(1, 1000):

    d = []
    n = N
    while n > 0:
        d.append(str(n % 4))
        n //= 4
    if not d:
        d = ["0"]
    q = "".join(d[::-1])

    if N % 4 == 0:

        if len(q) >= 2:
            q += q[-2:]
        else:
            q += q
    else:

        rem = (N % 4) * 2

        rem_digits = []
        r = rem
        while r > 0:
            rem_digits.append(str(r % 4))
            r //= 4
        if not rem_digits:
            rem_digits = ["0"]
        q += "".join(rem_digits[::-1])

    R = int(q, 4)

    if R < 479:
        max_N = max(max_N, N)

print(max_N)
