def def23(start, end, params="c"):
    if start == end or start + start % 3 == end:
        return 1

    elif start < end:
        return 0

    else:
        count = def23(start - 3, end, params + "a")

        if start % 3 == 0:
            count += def23(start // 3, end, params + "b")

        if "c" != params[-1]:
            count += def23(start + start % 3, end, params + "c")

        return count


print(def23(33, 1))
