for N in range(1, 10000):
    i = bin(N)[2:]
    if i.count("1") % 2 == 0:
        i = "10" + i[2:] + "10"
    else:
        i = "11" + i[2:] + "01"
    R = int(i, 2)
    if R > 102:
        print(N)
        break
