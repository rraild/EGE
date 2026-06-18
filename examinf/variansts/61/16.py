from sys import setrecursionlimit

setrecursionlimit(10**8)


def F(n):
    return 3 * (G(n - 4) + 5)


def G(n):
    if n < 8:
        return 3 * n

    return G(n - 3) + 2


print(F(12345))
