from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n == 1:
        return 1

    return F(n - 1) + 3 * G(n - 1) + n


def G(n):
    if n == 1:
        return 1

    return 11 * F(n - 1) + G(n - 1) * 2 - n * n


print(F(28) / G(14))
