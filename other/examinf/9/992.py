c = 0

with open("other/examinf/9/992.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))

        rep = [x for x in nums if nums.count(x) > 1]
        unrep = [x for x in nums if nums.count(x) == 1]

        if len(rep) > 0:
            sum_unique = sum(unrep)
            pr = 1
            for x in rep:
                pr *= x

            cond2 = (3 * sum_unique) <= pr

            if cond2:
                c += 1

print(c)
