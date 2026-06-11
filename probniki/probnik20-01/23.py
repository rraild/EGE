def f(start, end):
    if start > end or start == 10 or start == 15:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 1, end) + f(start * 3, end) + f(start * 2, end)


print(f(2, 12) * f(12, 55))
