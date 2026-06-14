res = []

for x in range(67):
    c1 = 3 * 81**3 + x * 81**2 + 2 * 81**1 + 1
    c2 = 1 * 67**3 + 7 * 67**2 + x * 67**1 + 4

    t = c1 + c2

    if t % 35 == 0:
        res.append(t // 35)

print(res[-1])
