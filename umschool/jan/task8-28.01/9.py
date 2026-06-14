from itertools import permutations

s = "СЕРПОАВЫЙ"
vowels = "ЕОАЫ"
consonants = "СРПВЙ"
count = 0

for p in permutations(s, 3):
    t = True
    for i in range(2):
        if (p[i] in vowels) == (p[i + 1] in vowels):
            t = False
            break
    if t:
        count += 1

print(count)
