for n in range(700_001, 700_001 + 1000):
    F = 0
    for i in range(2, n):
        if n % i == 0:
            F = n // i - i
            break

    if F != 0 and F % 9 == 0:
        print(n, F)
