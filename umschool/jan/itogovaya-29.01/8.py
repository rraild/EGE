from turtle import bk, done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 15

for i in range(2):
    fd(18 * k)
    rt(90)
    fd(16 * k)
    rt(90)

up()
fd(28 * k)
left(270)
bk(10 * k)
pendown()

for i in range(4):
    fd(37 * k)
    rt(90)
    fd(46 * k)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
