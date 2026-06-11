results = []

for y in range(9, 18):
    for x in range(y):
        c1 = 5 * 18**3 + x * 18**2 + y * 18**1 + 10
        c2 = 1 * y**3 + 8 * y**2 + x * y**1 + 7

        results.append(c1 + c2)

print(len(set(results)))
