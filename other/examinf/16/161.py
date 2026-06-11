def F(n):
    if n >= 2022:
        return n
    else:
        return F(n + 5) + 7


print(F(45) - F(49))
