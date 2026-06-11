import itertools


def f(x, y, z, w):
    return ((not x and not z) or z) or (y and not (y or w))


res = []

for t in itertools.product([0, 1], repeat=5):
    rows = [[1, t[0], 1, t[1]], [1, 0, t[2], t[3]], [t[4], 0, 0, 0]]

    if len(set(map(tuple, rows))) != 3:
        continue

    for p in itertools.permutations("xyzw"):
        if [f(**dict(zip(p, r))) for r in rows] == [0, 1, 0]:
            res.append("".join(p))

print((set(res)))
