def to31(n):
    digits = []
    while n > 0:
        digits.append(n % 31)
        n //= 31
    return digits


c = 3 * 289**2024 + 81 * 49**121 - 9 * 16**81 - 6011
d = to31(c)
print(sum(d for d in d if d <= 17))
