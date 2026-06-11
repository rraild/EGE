Q = list(range(18 * 10, 32 * 10 + 1))
P = list(range(5 * 10, 20 * 10 + 1))
A = list(range(0, 10000))

for x in range(0, 10000):
    f = ((x in A) <= (x in P)) or (x in Q)
    if not f:
        A.remove(x)


print((max(A) - min(A)) / 10)
