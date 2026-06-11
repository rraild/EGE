f = [0] * 10000

for n in range(10000):
    if n < 3:
        f[n] = 1

    if n > 3:
        f[n] = f[n - 2] * (n // 3)


print(f[16])
