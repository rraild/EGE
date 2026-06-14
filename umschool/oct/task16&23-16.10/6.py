f = [0] * 10000

for n in range(10000):
    if n < 3:
        f[n] = 3

    if n >= 3:
        f[n] = 2 * n + 5 + f[n - 2]


print(f[3027] - f[3023])
