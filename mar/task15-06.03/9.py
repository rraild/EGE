mn_A = 100000

for x in range(1, 30000):
    y = 90000 - 3 * x
    if y > 0:
        mx = max(x, y)
        if mx < mn_A:
            mn_A = mx

print(mn_A + 1)
