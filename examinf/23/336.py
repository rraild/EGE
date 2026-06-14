def f(current, end, last_cmd):
    if current > end:
        return 0
    if current == end:
        return 1

    res = f(current + 3, end, "A") + f(current * 7, end, "C")

    if last_cmd != "A":
        res += f(current * 5, end, "B")

    return res


print(f(1, 1000, ""))
