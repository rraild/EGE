ans = 0
a_list = [[int(d) for d in x.split()] for x in open("other/examinf/9/925.txt")]

for a in a_list:
    c = [a.count(x) for x in set(a)]
    c1 = c.count(2) == 2 and c.count(1) == 2

    if c1:
        rep = sorted([x for x in set(a) if a.count(x) == 2])
        unq = [x for x in a if a.count(x) == 1]

        m_r = rep[1]

        p_u = 1
        for x in unq:
            p_u *= x

        if m_r**2 > p_u:
            ans += 1

print(ans)
