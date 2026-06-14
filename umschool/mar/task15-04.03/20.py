P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

A = set(range(1000))

for x in range(1000):
    f = ((x in A) <= (x not in P)) and ((x not in Q) <= (x not in A))
    if not f:
        A.remove(x)

print(len(A))
