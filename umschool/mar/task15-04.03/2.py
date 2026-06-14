Q = list(range(10 * 10, 55 * 10 + 1))
P = list(range(4 * 10, 20 * 10 + 1))
A = []

for x in range(0, 10000):
    f = (x in A) or ((x not in P) <= (x not in Q))
    if not f:
        A.append(x)

print((max(A) - min(A)) / 10)
