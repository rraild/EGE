with open("dec/task9&17-24.12/8.txt") as f:
    seq = [int(x) for x in f.read().split()]

    max6 = max(x for x in seq if str(x)[-1] == "6")

    count = 0
    max_sum_sq = 0

    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i + 1]
        if (str(a)[-1] == "6") ^ (str(b)[-1] == "6"):
            sum_sq = a**2 + b**2
            if sum_sq < max6**2:
                count += 1
                if sum_sq > max_sum_sq:
                    max_sum_sq = sum_sq

    print(count, max_sum_sq)
