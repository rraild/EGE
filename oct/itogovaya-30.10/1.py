def F(n):
    if n < 2:
        return 0

    if n % 4 > 0 and n > 2:
        return F(n - 1 - (n % 4)) + n

    if n % 4 == 0 and n > 2:
        return 2 * F(n - 1) - 1


print(F(50))
