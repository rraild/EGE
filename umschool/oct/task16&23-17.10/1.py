def F(n):
    if n == 3:
        return 3

    if n > 3:
        return 4 * F(n - 1) + 4 * G(n - 1)  # type: ignore


def G(n):
    if n == 3:
        return 3

    if n > 3:
        return n + 2 * F(n - 1) + 2 * G(n - 1)


print(G(9))
