for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((w and x) or ((y <= z) <= (w <= x))):
                    print(w, x, y, z)
