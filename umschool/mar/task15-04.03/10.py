def Del(n, m):
    return n % m == 0


B = range(45, 90 + 1)
c = 0

for A in range(1, 1000):
    t = True
    for x in range(1, 2000):
        f = Del(x, 52) and not (not (x in B) or Del(x, A))

        if f:
            t = False
            break

    if t:
        c += 1

print(c)
