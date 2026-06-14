def F(n):
    if n == 1:
        return 2

    if n == 2:
        return 3

    if n % 2 != 0 and n > 2:
        return int((F(n - 2) + F(n - 2)) / 7)

    if n % 2 == 0 and n > 2:
        return 7 * n - int(F(n - 1) / 2 + 5)


print(F(40))
