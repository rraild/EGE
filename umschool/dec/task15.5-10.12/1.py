R = list(range(35, 50 + 1))
Q = list(range(5, 15 + 1))
P = list(range(10, 40 + 1))
A = []
for x in range(1, 100):
    if not (((x in A) or (x in P)) or ((x in Q) <= (x in R))):
        A.append(x)

print(A)
print(A[-1] - A[0] + 1)
