with open("dec/task26-07.12/2.txt") as f:
    n = int(f.readline())
    a = [int(s) for s in f]
    a.sort(reverse=True)
    sale1 = sum(a[: n // 3]) * 0.5
    a.sort()
    sale2 = sum(a[: n // 3]) * 0.5
    print(int(sum(a) - sale1), int(sum(a) - sale2))
