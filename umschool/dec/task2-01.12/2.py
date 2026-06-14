print("z x y")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x or y) <= (y == z)) == 0:
                print(z, x, y)
