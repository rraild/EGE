s = 654**25 + 927**13 + 243**5 - 44**2 + 2025

cnt = 0

while s > 0:
    if s % 25 > 9:
        cnt += 1
    s //= 25

print(cnt)
