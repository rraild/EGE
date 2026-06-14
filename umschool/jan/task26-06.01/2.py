with open("jan/task26-06.01/2.txt") as f:
    n = int(f.readline())
    boxes = sorted([int(s) for s in f], reverse=True)
    gift = [boxes[0]]

    for box in boxes:
        if gift[-1] - box >= 5:
            gift.append(box)

    print(len(gift), min(gift))
