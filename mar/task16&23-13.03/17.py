def f(start, end, mult_count):
    if start > end or mult_count > 2:
        return 0

    if start == end:
        return 1 if mult_count == 2 else 0

    res = f(start + 2, end, mult_count)
    res += f(start + 3, end, mult_count)
    res += f(start * 2, end, mult_count + 1)
    res += f(start * 3, end, mult_count + 1)

    return res


print(f(1, 51, 0))
