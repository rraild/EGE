with open("dec/task9&17-24.12/14+.txt") as f:
    nums = list(map(int, f.read().split()))

    res = []

    for i in range(len(nums) - 1):
        x, y = nums[i], nums[i + 1]
        if len(str(x)) == int(str(x)[0]) and len(str(y)) == int(str(y)[0]):
            res.append(x + y)

    if res:
        print(f"{len(res)}{min(res)}")
