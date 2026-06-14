import ipaddress

net = ipaddress.ip_network("46.29.170.214/255.255.128.0", strict=False)

for ip in reversed(list(net)):
    if ip == net.network_address or ip == net.broadcast_address:
        continue

    octs = [int(x) for x in str(ip).split(".")]

    t = False
    for i in range(4):
        c = octs[i]
        oth = sum(octs) - c
        if c == oth:
            t = True
            break

    if t:
        print("".join(map(str, octs)))
        break
