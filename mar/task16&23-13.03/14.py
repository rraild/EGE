def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1

    res = f(start + 1, end)

    tens = (start // 10) % 10
    units = start % 10

    if tens < units:
        s = list(str(start))
        s[-1], s[-2] = s[-2], s[-1]
        swapped = int("".join(s))
        if swapped > start:
            res += f(swapped, end)

    return res


print(f(106, 163))
