from sys import setrecursionlimit

setrecursionlimit(1000000000)


def F(n):
    if n == 1:
        return 1
    return 2 * n + F(n - 1)


print(F(345678))
