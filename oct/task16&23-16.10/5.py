f = [0] * 10000

for n in range(10000):
    if n == 122:
        f[n] = 156

    if n > 1:
        f[n] = 2 * f[n - 1] + 4


print(f[2017] - 4 * f[2015])
