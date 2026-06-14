f = [0] * 100000

for n in range(100000):
    if n < 3:
        f[n] = 2

    if n > 2 and n % 2 == 0:
        f[n] = 2 * f[n - 2] - f[n - 1] + 2

    if n > 2 and n % 2 != 0:
        f[n] = 2 * f[n - 1] + f[n - 2] - 2


print(f[170])
