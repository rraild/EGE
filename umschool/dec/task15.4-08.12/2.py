Q = list(range(12, 29 + 1))
P = list(range(5, 41 + 1))
A = []
for x in range(1, 100):
    if not (((x in A) and (x in P)) or (not (x in Q))):
        A.append(x)

print(A)
print(A[-1] - A[0])
