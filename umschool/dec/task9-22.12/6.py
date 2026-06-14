from collections import Counter

with open("dec/task9-22.12/6.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        if len(set(n)) == 5:
            d = dict(Counter(n))
            reps = [x for x, c in d.items() if c == 2]
            unrep = [x for x, c in d.items() if c == 1]
            if max(unrep) + min(unrep) <= reps[0] * 2:
                ct += 1

    print(ct)
