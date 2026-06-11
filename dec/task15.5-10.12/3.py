Q = [x / 10 for x in range(60, 140 + 1)]
P = [x / 10 for x in range(20, 100 + 1)]
A = [x / 10 for x in range(10, 1000 + 1)]

for x0 in range(10, 1000 + 1):
    x = x0 / 10
    if not (((x in A) <= (x in P)) or (x in Q)):
        A.remove(x)


print(A)
print(A[-1] - A[0])
