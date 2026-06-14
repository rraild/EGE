def F(n):
    if n > 15:
        return n - 2
    if n < 15:
        return 4 * F(n + 2) - 6


print(F(6))
