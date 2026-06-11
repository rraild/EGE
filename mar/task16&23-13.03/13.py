def f(start, end):
    if start < end:
        return 0
    if start == end:
        return 1

    res = f(start - 1, end)
    res += f(start // 2, end)
    res += f(start // 3, end)

    return res


print(f(131, 41) * f(41, 3))
