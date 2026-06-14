def F(n):
    if n <= 14:
        return n * n * n + 22

    if n % 3 == 0 and n > 14:
        return F(n - 4) + F(n - 8)

    if n % 3 != 0 and n > 14:
        return F(n - 9) + n + 7


count = 0

for i in range(1, 200):

    if (
        "1" not in str(F(i))
        and "3" not in str(F(i))
        and "5" not in str(F(i))
        and "7" not in str(F(i))
        and "9" not in str(F(i))
    ):

        count += 1

print(count)
