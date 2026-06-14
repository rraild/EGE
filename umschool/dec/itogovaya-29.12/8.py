with open("dec/itogovaya-29.12/8.txt") as f:
    cnt = 0
    for s in f:
        nums = list(map(int, s.split()))

        if all(x % 2 != 0 for x in nums):
            mn = min(nums)
            if mn**2 > sum(nums) - mn:
                cnt += 1

    print(cnt)
