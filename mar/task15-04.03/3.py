Q = list(range(7 * 10, 15 * 10 + 1))
P = list(range(6 * 10, 16 * 10 + 1))
A = []

for x in range(0, 10000):
    f = ((x in P) or (x not in A)) and ((x not in Q) or (x in A))
    if not f:
        A.append(x)

print((max(A) - min(A)) / 10)
