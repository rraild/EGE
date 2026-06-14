def f(start, end):
    if start > end:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 2, end) + f(start * 3, end) + f(start**2, end)


print(f(3, 77))
