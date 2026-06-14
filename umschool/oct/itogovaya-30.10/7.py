itog = []


for n in range(42, 100):
    n2 = bin(n)[2:]
    if n2.count("1") % 2 == 0:
        n2 = "11" + n2[2:] + "1"

    else:
        n2 = "10" + n2[2:] + "1"

    R = int(n2, 2)
    itog.append(R)


print(min(itog))
