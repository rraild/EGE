Q = list(range(21, 58))
P = list(range(3, 39))
A = list(range(1, 1000))

for x in range(1000):
    f = ((x in Q) <= (x in P)) <= (not (x in A))

    if not f:
        A.remove(x)

print(A)
