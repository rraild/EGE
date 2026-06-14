def v4(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s


res = []

for n in range(491, 1000):
    quat = v4(n)
    b = bin(n)[2:]

    if int(quat[0]) % 2 == 0:
        b = b + "0"
        b = "10" + b[2:]
    else:
        b = "1" + b
        b_list = list(b)
        b_list[-2] = "0"
        b = "".join(b_list)

    r = int(b, 2)
    res.append(r)

print(min(res))
