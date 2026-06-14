def f(start, end):
    if start > end or start in {15, 30}:
        return 0
    if start == end:
        return 1
    return f(start + 2, end) + f(start + 3, end) + f(start**2, end)


print(f(3, 10) * f(10, 20) * f(20, 38))
