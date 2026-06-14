import itertools


def f(x, y, z, w):
    return (y <= (not (x <= z))) or w


for t in itertools.product([0, 1], repeat=7):
    t = [[t[0], 0, t[1], t[2]], [0, 1, t[3], t[4]], [1, t[5], t[6], 0]]
    for j in itertools.permutations("xyzw"):
        if [f(**dict(zip(j, p))) for p in t] == [0, 0, 0]:
            print(*j)
