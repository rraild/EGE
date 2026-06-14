def Del(n, m):
    return n % m == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        if not (Del(x, A) and (not (Del(x, 36)))) <= (not (Del(x, 12))):
            t = False
            break

    if t:
        print(A)
        break
