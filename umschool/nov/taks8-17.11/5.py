from itertools import permutations

c = 0
for i in permutations("ТАВРИЯ", r=5):
    s = "".join(i)
    if not (s.startswith("В")) and "ИЯ" not in s:
        c += 1
        print(c, s)
