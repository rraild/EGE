from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 15

for i in range(6):
    fd(10 * k)
    rt(270)

up()
fd(3 * k)
rt(270)
fd(5 * k)
left(90)
pendown()

for i in range(2):
    fd(10 * k)
    rt(270)
    fd(12 * k)
    rt(270)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
