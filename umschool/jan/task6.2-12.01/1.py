from turtle import bk, done, fd, lt, rt, speed

speed(0)
k = 20

lt(90)
for i in range(12):
    rt(60)
    fd(5 * k)
    lt(30)
    bk(5 * k)

done()
