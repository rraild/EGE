def to_6(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n //= 6
    return s


for x in range(1, 10001):
    c = 6**900 + 6**10 - x

    s = to_6(c)

    if s.count("3") == s.count("5"):
        print(x)
        break
