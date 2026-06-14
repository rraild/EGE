P = [x for x in range(10 * 10, 25 * 10 + 1)]
Q = [x for x in range(20 * 10, 40 * 10 + 1)]
A = []

for x in range(0, 1000):
    f = ((x in P) and (not (x in Q))) <= (x in A)
    if not f:
        A.append(x)

print((max(A) - min(A)) / 10)
