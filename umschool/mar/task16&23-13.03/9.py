from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    return 2 * (G(n - 3) + 13)


def G(n):
    if n < 6:
        return 2 * n

    return G(n - 2) + 3


print(F(14541))
