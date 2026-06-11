def f(start, end):
    if start < end or start == 15:
        return 0
    if start == end:
        return 1
    return f(start - 2, end) + f(start - 3, end) + f(start // 3, end)


print(f(48, 25) * f(25, 17) * f(17, 4))
