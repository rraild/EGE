import math

found = 0
n = 700001

while True:
    dmin = 0
    dmax = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            dmin = i
            dmax = n // i
            break

    if dmin != 0:
        m = dmin + dmax
        if m % 10 == 4:
            found += 1
            if found == 5:
                print(str(n) + str(m))
                break

    n += 1
