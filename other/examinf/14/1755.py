def to243(n):
    r = []
    while n > 0:
        r.append(n % 243)
        n //= 243
    return r[::-1]


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False

    return d > 1


s = to243(20 * 3**243 + 17 * 81**70 + 14 * 243**35 + 254 - 224 * 3**30)
print(len(list(d for d in s if d < 20 and is_prime(d))))
