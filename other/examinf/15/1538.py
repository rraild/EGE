P = [x for x in range(5 * 10, 47 * 10 + 1)]
Q = [x for x in range(12 * 10, 76 * 10 + 1)]
R = [x for x in range(58 * 10, 98 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in Q) <= (
        (x not in P) <= (((x not in R) and (x not in A)) <= (x not in Q))
    )

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
