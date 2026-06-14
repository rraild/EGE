with open("dec/task9-22.12/3.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        if len(set(n)) == len(n):
            if 3 * (max(n) + min(n)) >= (2 * (sum(n) - (max(n) + min(n)))):
                ct += 1

    print(ct)
