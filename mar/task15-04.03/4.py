Q = list(range(18 * 10, 30 * 10 + 1))
P = list(range(5 * 10, 16 * 10 + 1))
A = []

for x in range(0, 10000):
    f = ((x in P) or (x in Q)) <= (x in A)
    if not f:
        A.append(x)


print((max(A) - min(A)) / 10)
