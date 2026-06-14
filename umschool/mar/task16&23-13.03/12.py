def f(start, end):
    if start > end or start == 60:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 2, end) + f(start + 3, end) + f(start + 4, end)


print(f(56, 86))
