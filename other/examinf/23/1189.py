def f(start, end):
    if start < end or start == 28:
        return 0
    if start == end:
        return 1

    res = f(start - 2, end)

    if start % 2 == 0:
        res += f(start // 2, end)
    else:
        res += f(start - 3, end)

    return res


print(f(98, 1))
