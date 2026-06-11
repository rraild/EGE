def Del(n, m):
    if n % m == 0:
        return 1
    return 0


B = list(range(50, 81))
for A in range(1000):
    t = True
    for x in range(1000):
        f = ((x in B) <= (not (Del(x, 7)))) or (x + A >= 90)
        if not f:
            t = False
            break

    if t:
        print(A)
        break
