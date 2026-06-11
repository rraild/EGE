for n in range(1, 1000):
    s = bin(n)[2:]
    s += str(s.count("1") % 2)
    s += str(s.count("1") % 2)
    r = int(s, 2)
    if r > 1096:
        print(n)
        break
