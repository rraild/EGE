def F(start, end, com):
    if start > end:
        return 0

    if start == end and "".join(sorted(com)) == com:
        return 1

    if start < end:
        return (
            F(start * 3, end, com + "1")
            + F(start * 2, end, com + "2")
            + F(start + 2, end, com + "3")
            + F(start + 1, end, com + "4")
        )

    else:

        return 0


print(F(2, 25, ""))
