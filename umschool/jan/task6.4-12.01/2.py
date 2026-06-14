from turtle import bk, done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 100

for i in range(24):
    rt(90)
    fd(1 * k)
    left(45)
    bk(1 * k)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(5)


done()
