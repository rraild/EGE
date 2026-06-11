Q = [x / 10 for x in range(170, 540 + 1)]
P = [x / 10 for x in range(230, 1110 + 1)]
A = []
for x0 in range(10, 10000):
    x = x0 / 10
    if not (
        (x in Q) <= (((x in P) and (x in Q)) or (not (x in P) <= (x in A)))
    ):
        A.append(x)

print(A)
print(A[-1] - A[0])
