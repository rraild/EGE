for a in range(0, 1000):
    ok = True
    for x in range(0, 300):
        for y in range(0, 300):
            if not ((x >= 27) or (2 * x < 3 * y) or (a > (x + 2) * (y - 3))):
                ok = False
                break
        if not ok:
            break

    if ok:
        print(a)
        break
