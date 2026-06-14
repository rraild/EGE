def to_4(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s


for n in range(1, 1000):
    s = to_4(n)
    digits_sum = sum(int(d) for d in s)

    if digits_sum % 2 == 0:
        s = "13" + s[2:] + "0"
    else:
        s = "2" + s
        s = s[:-2] + "13"

    r = int(s, 4)

    if r == 167:
        print(n)
        break
