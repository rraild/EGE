def f(start, end, last_cmd, count):
    if start > end:
        return 0
    if start == end:
        return 1

    res = 0

    if last_cmd == 1:
        if count < 3:
            res += f(start + 1, end, 1, count + 1)
    else:
        res += f(start + 1, end, 1, 1)

    if last_cmd == 2:
        if count < 3:
            res += f(start * 3, end, 2, count + 1)
    else:
        res += f(start * 3, end, 2, 1)

    return res


print(f(1, 30, 0, 0))
