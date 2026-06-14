from turtle import done, dot, fd, left, rt, setpos, speed, up

speed(0)
left(90)

k = 50

for i in range(4):
    rt(90)
    fd(5 * k)

up()
for x in range(-0, 150):
    for y in range(-20, 5):
        setpos(x * k, y * k)
        dot(3)


done()
