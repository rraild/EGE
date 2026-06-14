import re

with open("mar/task10-02.03/2.txt", encoding="utf-8") as f:
    text = f.read()

    m = re.sub(r"[^a-zA-Zа-яА-ЯёЁ]", " ", text)

    words = m.split()
    c = 0

    for word in words:
        if len(word) == 5:
            c += 1

print(c)
