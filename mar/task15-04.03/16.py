A = list(range(3, 105 + 1))
B = [x for x in range(2, 206) if 206 % x == 0]

for y in range(2, 10000):
    C = [x for x in range(2, y) if y % x == 0]

    if C:
        for x in range(1, 10000):
            f = (x in C) <= ((x in A) and (x not in B))
            if not f:
                break
        else:
            print(y)
            break
