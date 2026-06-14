c = 0

with open("other/examinf/9/950.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))

        mx = max(nums)
        cond1 = nums.count(mx) == 1

        cond2 = len(set(nums)) < len(nums)

        oth = []
        t = False
        for x in nums:
            if x == mx and not t:
                t = True
                continue
            oth.append(x)

        avg = sum(oth) / len(oth)
        cond3 = mx > (avg * 3)

        if cond1 and cond2 and cond3:
            c += 1

print(c)
