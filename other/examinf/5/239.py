for n in range(1, 100000):
    r = bin(n)[2:]
    if r.count("1") % 2 != 0:
        r = r + "11"

    else:
        r = "11" + r

    if int(r, 2) > 102:
        print(n)
        break
