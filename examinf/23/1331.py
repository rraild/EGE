def f(start, end):
    if start < end or start == 15:
        return 0
    if start == end:
        return 1
    return f(start - 2, end) + f(start - 5, end) + f(start // 3, end)


print(f(50, 35) * f(35, 20) * f(20, 8))
