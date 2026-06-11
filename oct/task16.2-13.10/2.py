f = [0] * 10000

for n in range(10000):
    if n < 4 or n % 2 != 0:
        f[n] = 1

    if n > 3 and n % 2 == 0:
        f[n] = f[n - 1] + f[n - 2] + f[n - 3]

print(f[4008] - f[4002])
