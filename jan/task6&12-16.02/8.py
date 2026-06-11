from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 10


for _ in range(1):
    fd(11 * k)
    rt(90)
    fd(32 * k)
    rt(90)

fd(4 * k)
rt(90)
fd(10 * k)
for _ in range(2):
    rt(90)
    fd(2 * k)
left(90)
fd(1 * k)
left(90)
fd(20 * k)
for _ in range(2):
    left(90)
    fd(12 * k)
rt(90)
fd(7 * k)
rt(90)
fd(34 * k)
rt(90)
fd(9 * k)
rt(90)
fd(18 * k)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
