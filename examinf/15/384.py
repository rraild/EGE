B = [x for x in range(24 * 10, 90 * 10 + 1)]
C = [x for x in range(47 * 10, 115 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = (x in C) <= (((x not in A) and (x in B)) <= (x not in C))

    if not f:
        A.append(x)

print(A[-1] / 10 - A[0] / 10)
