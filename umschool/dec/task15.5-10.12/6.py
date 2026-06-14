Q = [x / 10 for x in range(180, 340 + 1)]
P = [x / 10 for x in range(20, 160 + 1)]
A = []

for x0 in range(10, 10000 + 1):
    x = x0 / 10
    if not (((x in P) or (x in Q)) <= (x in A)):
        A.append(x)


print(A)
print(A[-1] - A[0])
