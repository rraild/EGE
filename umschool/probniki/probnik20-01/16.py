from sys import setrecursionlimit

setrecursionlimit(30000)


def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n - 1)


r = (2026 * F(2029) + F(2028)) // F(2027)
print(r)
