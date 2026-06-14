P = [x for x in range(17 * 10, 58 * 10 + 1)]
Q = [x for x in range(29 * 10, 80 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
