from turtle import done, dot, down, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 25

for i in range(8):
    fd(7 * k)
    rt(90)

up()
fd(2 * k)
rt(90)
fd(3 * k)
left(90)
down()
for _ in range(2):
    fd(6 * k)
    rt(90)
    fd(8 * k)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
