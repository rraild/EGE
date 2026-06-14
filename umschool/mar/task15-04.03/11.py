Q = list(range(20 * 10, 38 * 10 + 1))
P = list(range(7 * 10, 15 * 10 + 1))
A = list(range(0, 10000))

for x in range(0, 10000):
    f = ((x not in P) <= (x in Q)) or (x not in A)
    if not f:
        A.remove(x)

print(set([x // 10 for x in A]))
print(38 - 20)
