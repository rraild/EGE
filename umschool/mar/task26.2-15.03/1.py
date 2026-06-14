with open("mar/task26.2-15.03/1.txt") as f:
    f.readline()
    boxes = [int(s) for s in f]
    boxes.sort(reverse=True)
    gift = [boxes[0]]
    for box in boxes:
        if gift[-1] - box >= 5:
            gift.append(box)

print(len(gift), min(gift))
