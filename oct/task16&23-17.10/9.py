def f(start, end):
    if start > end:
        return 0

    if start == end:
        return 1

    if start < end:
        return f(start + 1, end) + f(
            int(bin(start)[2:] + bin(start % 8)[2:], 2), end
        )


print(f(1, int("10111110", 2)))
