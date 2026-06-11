with open("dec/task9&17-24.12/10.txt") as f:
    seq = [int(x) for x in f.read().split()]

    min_2digit = min(x for x in seq if 10 <= x <= 99)

    count = 0
    max_sum = 0

    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i + 1]
        if 10 <= a <= 99 and 10 <= b <= 99:
            s = a + b
            if s % min_2digit == 0:
                count += 1
                max_sum = max(max_sum, s)

    print(f"{count}{max_sum}")
