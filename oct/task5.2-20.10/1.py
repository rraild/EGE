for i in range(1, 10000):
    n = bin(i)[2:]

    if (n.count("1") % 2) == 0:
        n += "0"
    else:
        n += "1"

    if (n.count("1") % 2) == 0:
        n += "0"
    else:
        n += "1"

    r = int(n, 2)
    if r > 630:
        print(i)
        break
