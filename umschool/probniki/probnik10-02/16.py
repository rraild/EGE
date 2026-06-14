def F(n):
    if n <= 3:
        return 1

    if n % 2 == 0 and n > 3:
        return F(n / 5 - 3)

    if n % 2 != 0 and n > 3:
        return n**3


for x in range(100000):
    if F(x) > 559:
        print(F(x))
        break
