P = [x for x in range(3 * 10, 15 * 10 + 1)]
Q = [x for x in range(14 * 10, 25 * 10 + 1)]
A = list(range(10, 10000))

for x in range(1 * 10, 1000 * 10):
    f = ((x in P) == (x in Q)) <= (x not in A)

    if not f:
        A.remove(x)

print(list(x // 10 for x in A))
print(14 - 3, 25 - 15)
