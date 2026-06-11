from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 25


for i in range(6):
    fd(3 * k)
    rt(300)

fd(3 * k)
rt(270)
fd(2 * k)
rt(90)
pendown()
for _ in range(2):
    fd(3 * k)
    rt(270)
    fd(4 * k)
    rt(270)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
