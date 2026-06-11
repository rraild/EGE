def Del(n, m):
    return n % m == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        if not (
            (Del(x, A) and Del(x, 8)) <= ((not (Del(x, 8))) or Del(x, 240))
        ):
            t = False
            break

    if t:
        print(A)
        break
