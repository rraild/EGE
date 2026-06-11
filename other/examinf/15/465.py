P = [x for x in range(254 * 10, 800 * 10 + 1)]
Q = [x for x in range(410 * 10, 823 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = ((x in P) and (x not in A)) <= (x in Q)

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
