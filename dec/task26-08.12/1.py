with open("dec/task26-08.12/1.txt") as f:
    n = int(f.readline())
    boxes = [int(s) for s in f]
    boxes.sort(reverse=True)
    gift = [boxes[0]]
    for box in boxes[1:]:
        if gift[-1] - box >= 5:
            gift.append(box)

print(len(gift), min(gift))
