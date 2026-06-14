from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 10

for i in range(4):
    fd(19 * k)
    rt(90)
    fd(30 * k)
    rt(90)
up()
fd(2 * k)
rt(90)
fd(8 * k)
left(90)
pendown()
for i in range(4):
    fd(93 * k)
    rt(90)
    fd(27 * k)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
