with open("mar/task26.2-15.03/2.txt") as f:
    f.readline()
    data = sorted([int(x) for x in f], reverse=True)

    res = [data[0]]
    for x in data:
        if res[-1] - x >= 11:
            res.append(x)

print(len(res), res[-1])
