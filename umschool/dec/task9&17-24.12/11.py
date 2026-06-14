with open("dec/task9&17-24.12/11.txt") as f:
    data = [int(x) for x in f]
    res = []
    min_600 = min([x for x in data if abs(x) % 1000 == 600])

    for i in range(len(data) - 2):
        triple = data[i : i + 3]
        five_digit = sum(1 for x in triple if len(str(abs(x))) == 5)

        if five_digit <= 2 and sum(triple) >= min_600:
            res.append(sum(triple))

    print(len(res), min(res))
