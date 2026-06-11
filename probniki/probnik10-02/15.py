Q = [x for x in range(23 * 10, 40 * 10 + 1)]
P = [x for x in range(12 * 10, 25 * 10 + 1)]
A = []

for x in range(10, 100000):
    f = ((x in P) and (not (x in Q))) <= (x in A)

    if not (f):
        A.append(x)

print(list(x / 10 for x in A))
print(30 - 12)
