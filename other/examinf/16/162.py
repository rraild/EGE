from sys import setrecursionlimit

setrecursionlimit(1000000)


def F(n):
    if n <= 2:
        return n

    return n + F(n - 2)


print(F(2023) + F(2020))
