P = [x for x in range(25 * 10, 50 * 10 + 1)]
Q = [x for x in range(54 * 10, 75 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in Q) <= (((x in P) == (x in Q)) or ((x not in P) <= (x in A)))

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
