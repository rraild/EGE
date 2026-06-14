from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n > 40:
        return F(n - 4) + 3020

    return 3 * (G(n - 2) - 15)


def G(n):
    if n >= 301208:
        return 10 * n + 50

    return G(n + 7) - 21


print(F(5078))
