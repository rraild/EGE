def f(start, end):
    if start > end or start == 23:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 1, end) + f(start * 2, end)


print(f(4, 66) * f(66, 93))
