import math


def sum_digits(x):
    return sum(map(int, str(x)))


cnt = 0
with open("dec/task9&17-24.12/6.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))
        repeat = [x for x in nums if nums.count(x) > 1]

        if len(repeat) == 2:
            prod_repeat = math.prod(repeat)
            if oct(sum_digits(prod_repeat) ** 2)[-1] == "0":
                cnt += 1

print(cnt)
