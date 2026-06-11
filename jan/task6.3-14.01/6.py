from turtle import done, dot, down, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 20

for i in range(3):
    down()
    for i in range(2):
        fd(10 * k)
        rt(90)
        fd(10 * k)
        rt(90)

    up()

    fd(10 * k)
    rt(90)
    fd(5 * k)
    rt(90)


up()
for x in range(-100, 150):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(3)


done()
