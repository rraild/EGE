for i in range(1, 10000):
    n = bin(i)[2:]

    if (n.count("1") % 2) == 0:
        n += "0"
        n = "10" + n[2:]
    else:
        n += "11"
        n = "11" + n[2:]

    r = int(n, 2)
    if r < 99:
        print(i)
