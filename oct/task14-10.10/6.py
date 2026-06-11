a = 35**28 + 92**15 - 12**5
cnt = 0

while a > 0:
    if a % 5 == 3:
        cnt += 1

    a //= 5

s = ""

while cnt > 0:
    s += str(cnt % 9)
    cnt //= 9

s = s[::-1]
