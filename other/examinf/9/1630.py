mn = float("inf")

with open("other/examinf/9/1630.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))

        cond1 = (min(nums) ** 2) in nums

        pairs = 0
        for x in set(nums):
            pairs += nums.count(x) // 2
        cond2 = pairs >= 3

        if (cond1 + cond2) == 1:
            mn = min(mn, sum(nums))

print(mn)
