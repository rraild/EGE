itog = []


def to_base4(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n % 4) + s
        n //= 4
    return s


for n in range(1, 200):
    s = to_base4(n)
    if n % 4 == 0:
        add = s[-2:] if len(s) >= 2 else s
    else:
        add = to_base4((n % 4) * 2)
    R = int(s + add, 4)
    if R < 479:
        itog.append(n)

print(max(itog))
