from turtle import bk, fd, lt, pos, rt, tracer

tracer(0)

coords = []
for _ in range(8):
    fd(2)
    lt(540)
    bk(2)
    rt(450)
    fd(5)
    coords.append(pos())

# Формула Гаусса (площадь шнурка)
s = 0
for i in range(len(coords)):
    x1, y1 = coords[i]
    x2, y2 = coords[(i + 1) % len(coords)]
    s += x1 * y2 - x2 * y1

print(abs(s) / 2)
