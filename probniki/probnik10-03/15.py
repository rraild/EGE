def Del(x, A):
    return x % A == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        f = (Del(x, A) and (not (Del(x, 12)))) <= (not (Del(x, 18)))

        if not f:
            t = False
            break

    if t:
        print(A)
        break
