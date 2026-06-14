def f(start, end):
    if start > end or start == 20:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 2, end) + f(start * 3, end)


print(f(2, 24) * f(24, 100))
