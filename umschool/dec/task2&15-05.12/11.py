def Del(n, m):
    return n % m == 0


for A in range(1, 10000):
    t = True
    for x in range(1, 10000):
        if not ((Del(x, 2) <= (not (Del(x, 5)))) or (x + A >= 70)):
            t = False
            break

    if t:
        print(A)
        break
