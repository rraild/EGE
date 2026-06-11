from sys import setrecursionlimit

setrecursionlimit(100000)


def F(n):
    if n < 50:
        return n

    return F(n - 4) * (n - 9)


print(((F(56274) - 830 * F(56263)) // F(56259)))
