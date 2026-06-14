P = list(range(10, 21 + 1))
Q = list(range(13, 38 + 1))
R = list(range(18, 25 + 1))
A = []

for x in range(1000):
    f = (not ((x in Q) <= ((x in P) or (x in R)))) <= (
        not (x in A) <= (not (x in Q))
    )

    if not f:
        A.append(x)

print(A)
print(len(A))
