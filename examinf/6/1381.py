from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 10

for i in range(2):
    fd(28 * k)
    rt(90)
    fd(18 * k)
    rt(90)

up()
fd(14 * k)
rt(90)
fd(10 * k)
left(90)
pendown()
for i in range(2):
    fd(30 * k)
    rt(90)
    fd(7 * k)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
