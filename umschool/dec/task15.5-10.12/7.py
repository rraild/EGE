P = [x / 10 for x in range(130, 370 + 1)]
Q = [x / 10 for x in range(220, 510 + 1)]
A = []


def DEL(n, m):
    return n % m == 0


for x0 in range(10, 100000 + 1):
    x = x0 / 10
    if ((x in Q) <= (DEL(x, 18) or (x in P))) <= (x in A):
        A.append(x)


print(A)
print(51 - 37)
