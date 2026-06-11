def F(n):
    if n == 1:
        return 1
    return (3 * F(n - 1) - G(n - 1)) * 2


def G(n):
    if n == 1:
        return 1
    return F(n - 1) - 3 * G(n - 1) + 1


print(F(7))
