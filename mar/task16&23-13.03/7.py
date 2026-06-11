from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n == 5:
        return n * 5

    return 2 + F(n - 1) + 6 * G(n - 1)


def G(n):
    if n == 5:
        return n * 5
    return F(n - 1) - G(n - 1) + n * G(n - 1)


print(G(18))
