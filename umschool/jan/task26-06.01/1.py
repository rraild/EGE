with open("jan/task26-06.01/1.txt") as f:
    n = int(f.readline())
    data = [int(s) for s in f]
    data.sort(reverse=True)
    sum_f = sum(data[len(data) // 3 :])
    print(sum_f)

    sum_s = sum(data)

    for i in range(n):
        if (i + 1) % 3 == 0:
            sum_s -= data[i]

    print(sum_s)
