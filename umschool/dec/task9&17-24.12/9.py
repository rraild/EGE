with open("dec/task9&17-24.12/9.txt") as f:
    seq = [int(x) for x in f.read().split()]

    mn = min(seq)
    count = 0
    max_sum = 0

    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i + 1]
        if a % 123 == mn or b % 123 == mn:
            count += 1
            max_sum = max(max_sum, a + b)

    print(f"{count}{max_sum}")
