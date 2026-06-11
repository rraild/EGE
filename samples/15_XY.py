# наименьшее неотриц. A
# (x * y < A) or (5 * x < y) or (486 <= x)
# истинно при неотриц. x y

# y = 5 * x -> y = 5 * 486 = 2430
# x = 486


def check(A):
    for d_x in range(-100, 100):
        for d_y in range(-100, 100):
            x = 486 + d_x
            y = 2430 + d_y
            f = (x * y < A) or (5 * x < y) or (486 <= x)
            if f == 0:
                return 0
    return 1


for A in range(1180001 - 10_000, 10**10, 1):
    if check(A):
        print(A)
        break
