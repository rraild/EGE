import ipaddress

for mask_len in range(32, 15, -1):
    net = ipaddress.ip_network(f"132.118.34.161/{mask_len}", strict=False)

    c = 0
    for ip in net:
        if bin(int(ip)).count("1") == 13:
            c += 1

    if c == 35:
        mask_bin = f"{int(net.netmask):032b}"
        print(mask_bin.count("0"))
        break
