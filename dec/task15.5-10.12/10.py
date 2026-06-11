A = list(range(3, 54 + 1))
B = [i for i in range(2, 137) if 137 % i == 0]

for y in range(1, 10000):
    C = [i for i in range(2, y) if y % i == 0]
    if C:
        for x in range(1, 10000):
            if not ((x in C) <= ((x in A) and (not (x in B)))):
                break

        else:
            print(y)
