for n in range(1, 1000):
    s = bin(n)[2:]

    if s.count("1") % 2 == 0:
        s = "1" + s + "00"
    else:
        s = "11" + s

    r = int(s, 2)

    if r >= 412:
        print(n)
        break
