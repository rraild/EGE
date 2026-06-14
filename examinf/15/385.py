P = [x for x in range(16 * 10, 84 * 10 + 1)]
Q = [x for x in range(27 * 10, 43 * 10 + 1)]
A = list(range(10, 10000))

for x in range(1 * 10, 10000 * 10):
    f = ((x in A) <= (x in P)) or (x in Q)

    if not f:
        A.remove(x)

print(A[-1] / 10 - A[0] / 10)
