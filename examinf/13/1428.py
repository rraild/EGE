byte1 = 205
byte2 = 131

p = [0, 128, 192, 224, 240, 248, 252, 254, 255]

mn = None

for m in p:
    if (byte1 & m) != (byte2 & m):
        mn = m
        break

print(mn)
