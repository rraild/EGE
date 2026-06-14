P = {2, 4, 6, 7, 8, 10, 14}
Q = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14}

A = []

for x in range(1, 100):
    if (x in P) <= (x in Q):
        if x in Q:
            A.append(x)

print(sum(A))
