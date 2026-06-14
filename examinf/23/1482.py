def f(start, end):
    if start > end or start == 34:
        return 0
    if start == end:
        return 1
    return f(start + 2, end) + f(start + 5, end) + f(start * 2, end)


print(f(10, 26) * f(26, 52) * f(52, 78))
