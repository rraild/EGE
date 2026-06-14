def f(x, y, A):

    return (((y > A) or (x * y < 2 * A)) <= (A * y < 30)) or (
        (2 * y + 4 * x) < A
    )


kk = 0

for A in range(10000):

    flag = True

    for x in range(1, 101):

        for y in range(1, 101):

            if not f(x, y, A):

                flag = False

                break

        if not flag:

            break

    if flag:

        kk += 1

        if kk == 8:

            print(A)

            break
