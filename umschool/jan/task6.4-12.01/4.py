from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 25

for i in range(2):
    rt(45)
    fd(4 * k)
    for j in range(10):
        rt(45)
        fd(7 * k)
        rt(135)
        fd(4 * k)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
