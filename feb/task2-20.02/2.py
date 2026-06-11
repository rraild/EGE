import itertools


def f(x, y, z, w):
    return (x or y) and not (y == z) and not (w)


for t in itertools.product([0, 1], repeat=5):
    t = [[t[0], t[1], t[2], 1], [0, 1, 0, 0], [1, 0, 0, t[3]]]
    for j in itertools.permutations("xyzw"):
        if [f(**dict(zip(j, p))) for p in t] == [1, 1, 1]:
            print(*j)
