res = []
for n in range(1, 1000):
    b = bin(n)[2:]
    s_digits = b.count("1")

    if s_digits % 2 == 0:
        b = b + "10"
        b = "10" + b[2:]
    else:
        b = b + "01"
        b = "11" + b[2:]

    r = int(b, 2)
    if r <= 390:
        res.append(n)

print(max(res))
