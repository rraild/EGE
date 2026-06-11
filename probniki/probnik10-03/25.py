count = 0
n = 100001

while count < 6:
    v = 0
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            v = d + (n // d)
            break

    if v > 0 and v % 11 == 0:
        count += 1
        if count == 6:
            print(f"{n}{v}")

    n += 1
