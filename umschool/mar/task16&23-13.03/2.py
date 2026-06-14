from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n == 1:
        return 1

    return (2 * n - 2) * F(n - 1)


print(F(2555) / F(2553))
