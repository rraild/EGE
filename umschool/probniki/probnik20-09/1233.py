import itertools

print("x y z")
for x, y, z in itertools.product((0, 1), repeat=3):
    if not ((x == y) or (x <= (y and z))):
        print(x, y, z)
