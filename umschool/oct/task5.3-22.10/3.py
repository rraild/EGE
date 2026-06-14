for N in range(1, 10000):
    i = bin(N)[2:]
    if N % 2 == 0:
        sum_d = str(i.count("1"))
        i = i + bin(int(sum_d))[2:]
    else:
        i = "1" + i + "00"
    R = int(i, 2)
    if R > 843:
        print(N)
        break
