def f(start, end):
    if start > end or start == 35:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)


print(f(7, 13) * f(13, 15) * f(15, 51))
