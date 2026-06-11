def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


c = 0
for n in range(610_001, 610_001 + 100):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(n // i):
            print(n, n // i)
            c += 1
        break

    if c == 6:
        break
