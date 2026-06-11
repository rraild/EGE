c = 0
with open("nov/1.txt") as file:
    lst = (
        file.read()
        .replace("-", " ")
        .replace(".", " ")
        .replace(",", " ")
        .replace("…", " ")
        .replace("!", " ")
        .replace("?", " ")
        .replace(":", " ")
        .replace("»", " ")
        .replace("«", " ")
        .split()
    )
    for i in lst:
        if len(i) == 5:
            print(i)
            c += 1

print(c)
