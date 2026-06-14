from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n < 6:
        return n

    return F(n - 2) / 3 + 6 * n


print((F(2234) + 3 * F(2232)) // F(2230))
