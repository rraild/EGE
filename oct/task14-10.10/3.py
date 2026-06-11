s = 1024**789 + 256**678 - 64**567

cnt_4 = 0
while s > 0:
    if s % 5 == 4:
        cnt_4 += 1
    s = s // 5
print(cnt_4)
