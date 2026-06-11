Q = list(range(12, 22 + 1))
P = list(range(3, 13 + 1))
A = list(range(1, 100))

for x in range(1, 100):
    if not (((x in A) <= (x in P)) or (x in Q)):
        A.remove(x)

print(A)
print(A[-1] - (A[0]))
