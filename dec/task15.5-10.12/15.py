Q = [x for x in range(47, 71 + 1)]
P = [x for x in range(25, 55 + 1)]
R = [x for x in range(40, 54 + 1)]
A = []

for x in range(1, 20000):
    if (
        not (
            (((x in P) <= (not (x in Q))) and ((x in Q) <= (x in R)))
            or (x in A)
        )
        and x not in R
    ):
        A.append(x)

print(A)
print(len(A))
