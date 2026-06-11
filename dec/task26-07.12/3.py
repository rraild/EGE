with open("dec/task26-07.12/3.txt") as f:
    n = int(f.readline())
    a = [int(s) for s in f]
    a.sort(reverse=True)

    sale1 = sum(a[: n // 3])
    print(sum(a) - sale1)

    sale2 = 0
    for i in range(n):
        if (i + 1) % 3 == 0:
            sale2 += a[i]

    print(sum(a) - sale2)
