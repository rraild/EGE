with open("dec/task9&17-24.12/12.txt") as f:
    nums = list(map(int, f.read().split()))

    res = []

    for i in range(len(nums) - 1):
        x, y = nums[i], nums[i + 1]
        s = x + y

        if 100000 <= s <= 999999:
            if (int(x**0.5) ** 2 == x and x > 0) or (
                int(y**0.5) ** 2 == y and y > 0
            ):
                res.append(s)

    print(f"{len(res)}{max(res)}")
