import itertools


def f(x, y, z, w):
    return ((z <= y) == (x <= (not (w)))) and (x or y)


for t in itertools.product([0, 1], repeat=5):
    t = [[0, 1, 1, 1], [1, 0, 1, 0], [t[0], 0, 0, t[1]]]
    for j in itertools.permutations("xyzw"):
        if [f(**dict(zip(j, p))) for p in t] == [0, 1, 1]:
            print(j)
