l = [[int(d) for d in x.split()] for x in open("other/examinf/9/1633.txt")]
count = 0

for x in l:
    c1 = x.count(max(x)) == 1

    first, last = x[0], x[-1]
    mx, mn = max(x), min(x)
    c2 = (first != mn and first != mx) and (last != mn and last != mx)

    x.sort()
    p = x[3] * x[4] * x[5]
    c3 = p % x[0] == 0

    if [c1, c2, c3].count(True) == 1:
        count += 1

print(count)
