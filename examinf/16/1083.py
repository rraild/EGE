f = [0] * 14751
f[0] = 1

for n in range(1, 14751):
    if 1 - n == 0:
        n1 = f[0]
    else:
        n1 = -f[n - 1]

    f[n] = 2 * n1 + 3 * f[n - 1] + 2

res = f[14750]
ans = sum(int(d) for d in str(res))

print(ans)
