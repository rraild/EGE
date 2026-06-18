def divisors(n):
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


def prime(x):
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return False
    return x > 1


cnt = 0
for x in range(7_513_048 + 1, 10_000_000):
    d = divisors(x)
    if (len(d) == 1 or len(d) == 2) and all(prime(x) for x in d):
        if all("1" in str(x) and "6" in str(x) for x in d):
            print(x, max(d))
            cnt += 1
            if cnt == 5:
                break
