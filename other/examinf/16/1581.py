g = {}

for n in range(303800, -200, -1):
    if n > 303728:
        g[n] = n - 15
    else:
        g[n] = g[n + 8] / 2 - 109

f = {}

for n in range(-150, 2050):
    if n >= 128:
        f[n] = f[n - 5] + 1092
    else:
        f[n] = 5 * g[n - 7] + 29

print(int(f[2049]))
