from itertools import permutations

letters = "NORTHE"
count = 0

for p in permutations(letters, 4):
    word = "".join(p)

    if word[0] == "O":
        continue

    if "TH" in word:
        continue

    count += 1

print(count)
