s = 1296**625 * 216**125 + 36**25 - 6**5

cnt_5 = 0
while s > 0:
    if s % 6 == 5:
        cnt_5 += 1
    s = s // 6
print(cnt_5)
