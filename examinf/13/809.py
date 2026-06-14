import ipaddress

ip_node = "143.131.211.37"

for mask_len in range(32, -1, -1):
    net = ipaddress.ip_network(f"{ip_node}/{mask_len}", strict=False)

    c10 = 0
    for ip in net:
        if f"{int(ip):032b}".count("1") == 10:
            c10 += 1

    if c10 == 15:
        print(mask_len)
        break
