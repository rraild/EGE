def f(start, end):
    if start < end:
        return 0

    if start == end:
        return 1

    if start > end:
        return f(start - 1, end) + f(start // 2, end)


print(f(43, 10) * f(10, 1))
