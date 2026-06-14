with open("probniki/probnik20-01/input/17.txt") as f:
    c = 0
    mx = 0
    f = f.readlines()
    nums = [int(x) for x in f]
    avg = sum(nums) / len(nums)
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        if (a > avg or b > avg) and (a % 7 == 0 or b % 7 == 0):
            c += 1
            mx = max(mx, a * b)

    print(c, mx)
