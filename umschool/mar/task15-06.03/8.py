min_x = 180000

for x in range(0, 60001):
    y2 = 180000 - 3 * x
    if y2 >= 0 and y2 % 2 == 0:
        y = y2 // 2
        if x >= y:
            if x < min_x:
                min_x = x

print(min_x - 1)
