print("x y z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (
                    (
                        (
                            ((x and not w) <= (w <= z <= y))
                            and (not ((not y) <= w))
                        )
                        or (x and not (x <= z))
                    )
                    == (z == (not (z <= y)))
                ):
                    print(w, x, z, y)
