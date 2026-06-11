res = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "1" + b + "00"

    else:
        b = b + bin(b.count("1"))[2:]

    r = int(b, 2)
    if r > 205:
        res.append((r, n))

print(min(res))
