def f(start, end):
    if start > end or start == 35:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 1, end) + f(start * 3, end) + f(start * 4, end)


print(f(3, 10) * f(10, 70))
