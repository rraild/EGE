for i in range(1, 10000):
    n = bin(i)[2:]
    if i % 2 == 0:
        r = n + "01"
    else:
        r = n + "10"
    r_dec = int(r, 2)
    if r_dec > 101:
        print(r_dec)
        break
