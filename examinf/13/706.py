import ipaddress

ip1 = ipaddress.ip_address("120.91.176.213")
ip2 = ipaddress.ip_address("120.91.174.205")

res = 0

for mask_len in range(32, -1, -1):
    net1 = ipaddress.ip_network(f"{ip1}/{mask_len}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{mask_len}", strict=False)

    if net1 == net2:
        mask_str = str(net1.netmask)
        third_byte = int(mask_str.split(".")[2])
        res = max(res, third_byte)

print(res)
