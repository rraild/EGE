with open("dec/task9&17-24.12/5.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        if all(x % 2 == 0 for x in n):
            if min(n) ** 2 <= sum(n) - min(n):
                ct += 1

    print(ct)
