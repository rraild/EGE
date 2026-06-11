import ipaddress

ip1 = ipaddress.ip_address("120.91.85.213")
ip2 = ipaddress.ip_address("120.91.89.205")

max_third_byte = 0

for mask_len in range(32, -1, -1):
    net1 = ipaddress.ip_network(f"{ip1}/{mask_len}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{mask_len}", strict=False)

    if net1 == net2:
        mask_str = str(net1.netmask)
        third_byte = int(mask_str.split(".")[2])
        max_third_byte = max(max_third_byte, third_byte)

print(max_third_byte)
