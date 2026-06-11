def to_3(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


for n in range(4, 1000):
    s = to_3(n)

    if s.endswith("10"):
        s = "2" + s
    else:
        s = "1" + s

    r = int(s, 3)

    if r > 130:
        print(n)
        break
