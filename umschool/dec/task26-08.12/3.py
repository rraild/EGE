with open("dec/task26-08.12/3.txt") as f:
    n = int(f.readline())
    boxes = []
    for s in f:
        lens, color = s.split()
        boxes.append([int(lens), color])

    boxes.sort(reverse=True)
    blocks = []
    while boxes != []:
        gift = [boxes[0]]
        del boxes[0]

        for box in boxes[:]:
            if gift[-1][0] - box[0] >= 8 and gift[-1][1] != box[1]:
                gift.append(box)
                boxes.remove(box)

        blocks.append(gift)

print(len(blocks), len(blocks[0]))
