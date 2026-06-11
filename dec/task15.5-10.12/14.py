D = [x / 10 for x in range(280, 690 + 1)]
C = [x / 10 for x in range(400, 910 + 1)]
A = []

for x0 in range(1, 20000):
    x = x0 / 10
    if not (((x in D) <= (((x not in C) and (x not in A)) <= (x not in D)))):
        A.append(x)

print(A)
print(A[-1] - A[0])
