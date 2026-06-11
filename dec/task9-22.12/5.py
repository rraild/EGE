from collections import Counter

with open("dec/task9-22.12/5.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        if len(set(n)) < len(n):
            d = dict(Counter(n))
            unrep = [x for x, c in d.items() if c == 1]
            if sum(unrep) % 2 != 0:
                ct += 1

    print(ct)
