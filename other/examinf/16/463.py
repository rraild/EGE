f = [0] * 1000
f[1] = f[2] = 1

for n in range(3, 1000):
    f[n] = 3 * f[n - 2] + f[n - 1]


res = f[999] / f[995]
print(int(res))
