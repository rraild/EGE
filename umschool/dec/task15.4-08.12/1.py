Q = list(range(17, 91 + 1))
P = list(range(10, 47 + 1))
A = []
for x in range(1, 100):
    if not (((x in P) and (x in Q)) <= (x in A)):
        A.append(x)  # наименьшая длина

print(A)
print(print(A[-1] - A[0]))
