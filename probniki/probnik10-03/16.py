def F(n):
    if n < 4:
        return 3
    return F(n - 3) * (n * 2 + 7)


print(F(11))
