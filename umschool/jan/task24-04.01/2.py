with open("jan/task24-04.01/2.txt") as f:
    s = f.read()
    s = s.replace("-", "*")
    a = s.split("*")
    ar = ""
    mx_ar = []
    for x in a:
        if x and x[0] != "0":
            ar += x + "*"

        elif x == "0":
            ar += str(int(x)) + "*"

        elif len(x) > 1 and x[0] == "0":
            ar += "0*"
            mx_ar = max(mx_ar, ar, key=len)
            ar = str(int(x)) + "*"

        else:
            ar = ""

        mx_ar = max(ar, mx_ar, key=len)

    print(mx_ar)
    print(len(mx_ar) - 1)
