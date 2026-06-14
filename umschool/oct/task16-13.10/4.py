def F(n):
    if n < 4:
        return 4 * n - 1

    elif n % 2 == 0 and n >= 4:
        return F(n - 2) + 2 * n

    elif n % 2 != 0 and n >= 4:
        return F(n - 4) + 4 * n + 5


print(F(62))
