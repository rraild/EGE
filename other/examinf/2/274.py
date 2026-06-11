import itertools


def f(x, y, z, w):
    return (x or y or z) <= (x and (y or w))


for t in itertools.product([0, 1], repeat=5):
    t = [[1, 0, t[0], 0], [t[1], 1, 1, t[2]], [1, 1, t[3], 1]]
    for j in itertools.permutations("xyzw"):
        if [f(**dict(zip(j, p))) for p in t] == [0, 0, 0]:
            print(j)
