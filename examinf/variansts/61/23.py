def f(start, end):
    if start > end or start == 8:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 1, end) + f(start + 3, end) + f(start * 2, end)


print(f(2, 5) * f(5, 13))
