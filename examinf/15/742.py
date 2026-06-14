P = [x for x in range(43 * 10, 49 * 10 + 1)]
Q = [x for x in range(44 * 10, 53 * 10 + 1)]
A = list(range(10, 10000))

for x in range(1 * 10, 1000 * 10):
    f = ((x in A) <= (x in P)) or (x in Q)

    if not f:
        A.remove(x)

print(list(x / 10 for x in A))
print(53 - 43)
