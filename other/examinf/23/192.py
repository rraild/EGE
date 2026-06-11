def f(current, end, last_cmd):
    if current > end:
        return 0
    if current == end:
        return 1

    res = f(current + 3, end, "B") + f(current * 4, end, "C")

    if last_cmd != "C":
        res += f(current + 2, end, "A")

    return res


print(f(1, 50, ""))
