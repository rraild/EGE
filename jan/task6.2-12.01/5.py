from turtle import done, dot, fd, lt, rt, setpos, tracer, up

tracer(0)

k = 20

lt(90)
for i in range(12):
    fd(5 * k)
    rt(120)

up()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot(3)


done()
