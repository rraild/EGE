def F(n):
    if n <= 3:
        return n**3

    if n % 2 == 0 and n > 3:
        return n + 2 + 8 * F(n - 2)

    if n % 2 != 0 and n > 3:
        return 17 * n + F(n - 3) - F(n - 4) + 8


c = 0

for i in range(134, 929):
    if F(i) % 6 == 0:
        c += 1


print(c)
