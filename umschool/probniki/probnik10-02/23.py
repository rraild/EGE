def f(start, end):
    if start > end or start == 28:
        return 0

    if start == end:
        return 1

    return f(start + 1, end) + f(start * 2, end)


print(f(2, 10) * f(10, 35))
