import itertools


def f(x, y, z, w):
    return (x and (not (y))) and (w <= z)


for t in itertools.product([0, 1], repeat=5):
    t = [[0, t[0], t[1], 1], [0, t[2], 1, 1], [1, t[3], t[4], 1]]
    for j in itertools.permutations("xyzw"):
        if [f(**dict(zip(j, p))) for p in t] == [1, 1, 1]:
            print(*j)
