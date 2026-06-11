from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n >= 2025:
        return n

    return n // 2 + F(n + 3)


print(F(2020) - F(2023))
