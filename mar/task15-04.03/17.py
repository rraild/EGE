I = list(range(9, 20 + 1))
N = list(range(6, 26 + 1))
F = list(range(4, 38 + 1))

O = []

for x in range(-100, 100):
    f = ((2 * x not in I) and (x in N)) <= ((x not in F) or (x in O))

    if not f:
        O.append(x)

print(O)
print(O[-1] - O[0])
