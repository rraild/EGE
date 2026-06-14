def Cel(n, m):
    return n // m


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        if not ((Cel(x, 50) > 3) or (not (Cel(x, 13))) or (Cel(x, A) > 6)):
            t = False
            break

    if t:
        print(A)
        break
