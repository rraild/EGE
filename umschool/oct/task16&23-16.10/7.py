f = [0] * 10000

for n in range(10000):
    if n < 6:
        f[n] = n

    if n >= 6:
        f[n] = f[n - 2] // 3 + 6 * n


print((f[2765] + 3 * f[2763]) / f[2759])
