P = [x for x in range(15 * 10, 40 * 10 + 1)]
Q = [x for x in range(21 * 10, 63 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in P) <= (((x in Q) and not (x in A)) <= (not (x in P)))

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
