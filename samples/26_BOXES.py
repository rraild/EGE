with open("other/examinf/26/1303.txt") as f:
    n = int(f.readline())
    boxes = sorted([int(x) for x in f], reverse=True)

    gift = [boxes[0]]
    for box in boxes:
        if gift[-1] - box >= 9:
            gift.append(box)

print(len(gift), gift[-1])
