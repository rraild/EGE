g = {}

for n in range(221337 + 11, -200, -1):
    if n >= 221337:
        g[n] = 2 * n + 50
    else:
        g[n] = g[n + 11] - 48

f = {}

for n in range(-150, 5079):
    if n > 30:
        f[n] = f[n - 6] + 2048
    else:
        f[n] = 3 * (g[n - 5] + 13)

print(f[5078])
