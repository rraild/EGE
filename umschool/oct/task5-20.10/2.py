for N in range(10000):
    s = str(bin(N))[2:]
    s = s + s[-1]

    if (str(bin(N))[2:]).count("1") % 2 == 0:
        s = s + "0"
    else:
        s = s + "1"

    if s.count("1") % 2 == 0:
        s = s + "0"
    else:
        s = s + "1"

    r1 = int(s, 2)

    if r1 > 130:
        print(N)
        break
