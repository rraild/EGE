from turtle import (
    begin_fill,
    done,
    end_fill,
    fd,
    getcanvas,
    left,
    pendown,
    rt,
    speed,
)

pendown()
speed(0)
begin_fill()
left(90)

k = 5

rt(90)
for i in range(3):
    rt(45)
    fd(10 * k)
    rt(45)

rt(315)
fd(10 * k)

for i in range(2):
    rt(90)
    fd(10 * k)

end_fill()

c = 0
canvas = getcanvas()
for x in range(-100, 100):
    for y in range(-100, 100):
        # print(x, y, canvas.find_overlapping(x * k, y * k, x * k, y * k))
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            c += 1

print(c)
done()
