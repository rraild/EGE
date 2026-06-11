P = list(range(27 * 10, 130 * 10 + 1))
Q = list(range(50 * 10, 62 * 10 + 1))
R = list(range(38 * 10, 94 * 10 + 1))
A = []

for x in range(0, 10000):
    f = ((x not in P) or (x in Q)) or ((x not in A) <= (x not in R))
    if not f:
        A.append(x)


print((max(A) - min(A)) / 10)
