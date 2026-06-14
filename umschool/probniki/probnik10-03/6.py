from turtle import bk, done, dot, fd, lt, rt, setpos, tracer, up

tracer(0)
lt(90)

k = 12
for i in range(10):
    fd(6 * k)
    rt(90)
    bk(2 * k)
    rt(90)

rt(90)
fd(4 * k)

for i in range(7):
    lt(90)
    fd(4 * k)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)

done()
