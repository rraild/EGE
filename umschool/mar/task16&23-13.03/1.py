from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n == 1:
        return 1

    return n * F(n - 1)


print(((F(3000) // 150) + F(2999)) // F(2998))
