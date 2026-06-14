import ipaddress

net = ipaddress.ip_network("111.222.0.124/255.255.224.0", strict=False)

for ip in reversed(list(net)):
    b = f"{int(ip):032b}"
    if (b.count("1") * b.count("0")) % 2 != 0:
        print(sum(ip.packed))
        break
