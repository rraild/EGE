B = [x for x in range(23 * 10, 37 * 10 + 1)]
C = [x for x in range(41 * 10, 73 * 10 + 1)]
A = []

for x in range(1 * 10, 1000 * 10):
    f = not (((x not in B) <= (x in C)) <= (x in A))

    if f:
        A.append(x)

print(A)
print(A[-1] / 10 - A[0] / 10)
