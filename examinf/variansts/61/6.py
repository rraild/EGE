from turtle import bk, done, dot, down, fd, lt, rt, setpos, tracer, up

tracer(0)
down()
lt(90)
k = 25

for _ in range(2):
    fd(20 * k)
    lt(270)
    bk(15 * k)
    rt(90)

up()
fd(10 * k)
rt(90)
bk(20 * k)
lt(90)
down()

for _ in range(2):
    fd(6 * k)
    rt(90)
    fd(6 * k)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
