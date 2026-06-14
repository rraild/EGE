P = list(range(20, 151))
Q = list(range(40, 101))
R = list(range(30, 121))
S = list(range(10, 81))
T = list(range(60, 201))
U = list(range(90, 171))

A = []

for x in range(0, 1001):

    f = ((x in P) or (x in Q)) or (
        (not (x in A)) <= ((x in R) and (x in S) or (x in T) and (x in U))
    )

    if not f:
        A.append(x)

print(A)
