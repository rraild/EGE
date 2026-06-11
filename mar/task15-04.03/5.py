R = list(range(12 * 10, 30 * 10 + 1))
Q = list(range(8 * 10, 15 * 10 + 1))
P = list(range(10 * 10, 20 * 10 + 1))
A = []

for x in range(0, 10000):
    f = ((x in A) or (x in P)) or ((x in Q) <= (x in R))
    if not f:
        A.append(x)


print((max(A) - min(A)) / 10)
