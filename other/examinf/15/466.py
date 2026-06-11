P = [x for x in range(117 * 10, 158 * 10 + 1)]
Q = [x for x in range(129 * 10, 180 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
