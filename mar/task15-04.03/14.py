P = list(range(20 * 10, 130 * 10 + 1))
Q = list(range(40 * 10, 100 * 10 + 1))
R = list(range(25 * 10, 120 * 10 + 1))
S = list(range(50 * 10, 150 * 10 + 1))

A = []

for x in range(0, 1001):

    f = (((x in P) or (x in Q)) and ((x not in A) and (x in R))) <= (x in S)

    if not f:
        A.append(x)

print(([x / 10 for x in A]))
