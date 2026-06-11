from turtle import bk, done, dot, fd, lt, rt, setpos, tracer, up

tracer(0)

k = 20

lt(90)
for i in range(16):
    fd(5 * k)
    lt(70)
    bk(2 * k)
    rt(10)

up()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot(3)


done()
