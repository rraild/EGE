P = [x / 10 for x in range(270, 1300 + 1)]
Q = [x / 10 for x in range(500, 620 + 1)]
R = [x / 10 for x in range(380, 940 + 1)]
A = []


for x0 in range(10, 10000 + 1):
    x = x0 / 10
    if not (((x not in P) or (x in Q)) or ((x not in A) <= (x not in R))):
        A.append(x)


print(A)
print(A[-1] - A[0])
