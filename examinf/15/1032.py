def Del(x, A):
    return x % A == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        f = (not (Del(x, 84)) or not (Del(x, 90))) <= (not (Del(x, A)))

        if not f:
            t = False
            break

    if t:
        print(A)
        break
