res = 0
mx = 0

for b in range(9, 500):
    n = 39 * 15**64 + 35**450 + 74 * 43**121 - 450035
    cnt = 0
    while n > 0:
        if n % b == 8:
            cnt += 1
        n //= b

    if cnt >= mx:
        mx = cnt
        res = b

print(res)
