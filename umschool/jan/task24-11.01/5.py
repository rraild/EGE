import string


def check(a, b):
    for i in range(len(a)):
        if not (a[i] in b):
            return False

    return True


f = open("jan/task24-11.01/5.txt")
d = {}
cc = [str(i) for i in range(1, 10)] + list(string.ascii_uppercase)
d = d.fromkeys(cc, 0)
o = 2

for i in cc:
    d[i] = o
    o += 1

a = []
cnt = 0
for x in f:
    x = x[:-1]
    if (
        x[0] != "0"
        and check(
            list(set(x)), [str(i) for i in range(0, 10)] + ["A", "B", "C", "D"]
        )
        and sorted(x)[-1] != "0"
        and int(x, d[sorted(x)[-1]]) % 15 == 0
    ):

        cnt += 1
        # print(x)

print(cnt)
