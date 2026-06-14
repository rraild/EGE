for n in range(1, 1000):
    s = bin(n)[2:]

    s += s[-1]

    if bin(n).count("1") % 2 == 0:
        s += "0"
    else:
        s += "1"

    if s.count("1") % 2 == 0:
        s += "0"
    else:
        s += "1"

    r = int(s, 2)
    if r > 144:
        print(n)
        break
