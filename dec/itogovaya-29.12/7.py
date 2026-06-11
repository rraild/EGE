with open("dec/itogovaya-29.12/7.txt") as f:
    nums = [int(x) for x in f]

    m16 = [x for x in nums if x % 16 == 0]
    avg = sum(m16) / len(m16)

    res = []

    for i in range(len(nums) - 2):
        triple = nums[i : i + 3]
        cnt = sum(1 for x in triple if x > avg)

        if cnt >= 2:
            res.append(sum(abs(x) for x in triple))

    print(f"{len(res)}{min(res)}")
