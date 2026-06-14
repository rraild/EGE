P = [x for x in range(1 * 10, 98 * 10 + 1)]
Q = [x for x in range(25 * 10, 42 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in Q) <= (((x not in P) and (x in Q)) <= (x in A))

    if not f:
        A.append(x)

print(sorted(set(list(x // 10 for x in A))))
print(A[-1] / 10 - A[0] / 10)
