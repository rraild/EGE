def r(n):

    n -= n % 8

    n2 = bin(n)[2:]

    n2 += str(n2.count("1") % 2)

    n2 += str(n2.count("1") % 2)

    return int(n2, 2)


for n in range(1, 1000):
    if r(n) < 86:

        print(bin(n)[2:])
