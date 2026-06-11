for n in range(11, 100):
    o = oct(n)[2:]
    if n % 5 == 0:
        o = o[:2] + o

    else:
        o1 = bin(n % 5)[2:]
        o = o + o1

    if int(o, 8) > 35000:

        print(n)
