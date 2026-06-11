Q = list(range(33 * 10, 88 * 10 + 1))
P = list(range(10 * 10, 49 * 10 + 1))
A = list(range(0, 10000))

for x in range(0, 10000):
    f = ((x in P) <= (x not in Q)) <= (x not in A)
    if not f:
        A.remove(x)


print((max(A) - min(A)) / 10)
