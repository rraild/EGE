from turtle import done, dot, fd, left, pendown, rt, setpos, tracer, up

pendown()
tracer(0)
left(90)

k = 25


for i in range(7):
    rt(90)
    fd(3 * k)
    for _ in range(2):
        left(90)
        fd(3 * k)

left(20)

for i in range(7):
    rt(90)
    fd(3 * k)
    for _ in range(2):
        left(90)
        fd(3 * k)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
