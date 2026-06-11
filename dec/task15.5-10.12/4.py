Q = [x / 10 for x in range(210, 570 + 1)]
P = [x / 10 for x in range(30, 380 + 1)]
A = [x / 10 for x in range(10, 1000 + 1)]

for x0 in range(10, 1000 + 1):
    x = x0 / 10
    if not (((x in Q) <= (not (x in P))) <= (not (x in A))):
        A.remove(x)


print(A)
print(A[-1] - A[0])
