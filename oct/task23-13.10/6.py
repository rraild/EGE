def f(start, end):
    if start < end:
        return 0

    if start == end:
        return 1

    if start > end:
        return f(start - 1, end) + f(start // 3, end)


print(f(33, 7) * f(7, 2))
