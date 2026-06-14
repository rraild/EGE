from itertools import permutations

c = 0
for i in permutations("БАВЛЫ", r=4):
    s = "".join(i)
    if not (s.startswith("В")) and "АЫ" not in s:
        c += 1
        print(c, s)
