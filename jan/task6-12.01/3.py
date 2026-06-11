from turtle import done, dot, fd, lt, rt, setpos, tracer, up

tracer(0)

k = 18

lt(90)
for i in range(9):
    fd(5 * k)
    rt(90)
    fd(4 * k)
    rt(90)

up()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot(4)


done()
