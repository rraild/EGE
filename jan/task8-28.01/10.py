from itertools import permutations

s = "СЕРБИЯ"
vowels = "ЕИЯ"
consonants = "СРБ"
count = 0

for p in permutations(s, 5):
    t = True
    for i in range(4):
        if (p[i] in vowels) == (p[i + 1] in vowels):
            t = False
            break
    if t:
        count += 1

print(count)
