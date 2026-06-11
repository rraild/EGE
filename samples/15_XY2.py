# При каком наибольшем целом A найдутся такие целые неотрицательные x и y,
# при которых выражение
# (4·x + y > 115) ∨ (x > 3·y) ∨ (x + 4·y < A)
# ложно?

# 4*x + y = 115 -> 4 * 3 * y + y = 115 -> 13y = 115 -> y = 8
# x = 3 * y -> 3 * 8 -> x = 24


def check(A):
    for d_x in range(-100, 200):
        for d_y in range(-100, 200):
            x = d_x + 24
            y = d_y + 8

            if x >= 0 and y >= 0:
                f = (4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < A)
                if f == 0:
                    return 1

    return 0


for A in range(1, 10**4, 1):
    if check(A):
        print(A)
