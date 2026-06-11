from itertools import permutations

s = "ЕРЕТИК"
words = set()

for p in permutations(s):
    word = "".join(p)

    t = True
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            t = False
            break

    if t:
        words.add(word)

print(len(words))
