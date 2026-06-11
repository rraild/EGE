import ipaddress

ip1 = ipaddress.ip_address("176.213.225.119")
ip2 = ipaddress.ip_address("176.213.195.58")

mx = 0

for mask_len in range(32, -1, -1):
    net1 = ipaddress.ip_network(f"{ip1}/{mask_len}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{mask_len}", strict=False)

    if net1 == net2:
        mask_str = str(net1.netmask)
        th = int(mask_str.split(".")[2])
        mx = max(mx, th)

print(mx)
