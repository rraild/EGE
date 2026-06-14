print("w y z x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if x and not (w) and (y or not (z)) == 1:
                    print(w, y, z, x)
