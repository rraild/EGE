s = 5**172 + 4**347 - 8**93
cnt_0 = 0
while s > 0:
    if s % 4 == 0:
        cnt_0 += 1
    s = s // 4

print(oct(cnt_0)[2:])
