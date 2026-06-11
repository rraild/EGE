from sys import setrecursionlimit

setrecursionlimit(100000000)


def F(n):
    if n == 0:
        return 0
    return 3 * n + F(n - 1)


for n in range(100000):
    if F(n) > 17_505_321:
        print(n)
        break
