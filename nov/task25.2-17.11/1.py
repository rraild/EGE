for i in range(200123, 200150 + 1):
    if int(i**0.5) != i**0.5:
        divisors = []
        for j in range(1, int(i**0.5) + 1):
            if j * j == i:
                divisors.append(j)

            elif i % j == 0:
                divisors.append(j)
                divisors.append(i // j)

            if len(divisors) > 4:
                break

        if len(divisors) == 4:
            divisors.sort()
            print(*divisors)
