with open("jan/task24.5-25.12/6.txt") as f:
    s = f.readline()

    s = s.replace("++", "+ +").replace("++", "+ +")
    s = s.replace("**", "* *").replace("**", "* *")
    s = s.replace("+*", "+ *").replace("+*", "+ *")
    s = s.replace("*+", "* +").replace("*+", "* +")
    a = s.split()

    max_buf = ""
    for x in a:
        x2 = x[:]
        if x[0] in "+*":
            x2 = x2[1:]

        if x[-1] in "+*":
            x2 = x2[:-1]

        x2 = x2.split("+")

        buf = ""
        for pod_summi in x2:
            if len(pod_summi) > 0 and eval(pod_summi) == 0:
                buf += pod_summi + "+"

            elif len(pod_summi) > 0:
                if "0*" in pod_summi:
                    buf = "0*" + pod_summi.split("0*")[-1]

                else:
                    buf = ""
            else:
                buf = ""

            max_buf = max(buf, max_buf, key=len)

    print(len(max_buf) - 1)
