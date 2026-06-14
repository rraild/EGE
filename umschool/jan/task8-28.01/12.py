from itertools import product

letters = "ВЕСНА"
count = 0

for p in product(letters, repeat=4):
    word = "".join(p)

    if word.count("В") != 1:
        continue

    if word[0] == "А":
        continue

    if word[-1] == "С":
        continue

    count += 1

print(count)
