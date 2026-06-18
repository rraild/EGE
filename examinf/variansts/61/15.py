P = list(range(15 * 10, 70 * 10))
Q = list(range(40 * 10, 100 * 10))
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in P) <= ((x in A) or ((not (x in A)) and (x in Q)))

    if not f:
        A.append(x)

print(A)
print(A[-1] - A[0])
