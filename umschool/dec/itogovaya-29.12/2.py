for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((y <= z) <= (x and y)) and (x <= w):
                    print(z, x, w, y)
