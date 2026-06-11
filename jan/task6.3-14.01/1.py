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
k = 100
for i in range(21):
    fd(137 * k)
    rt(120)

end_fill()

c = 0
canvas = getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            c += 1

print(c)
done()
