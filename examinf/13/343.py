import ipaddress

ip1 = ipaddress.ip_address("121.171.5.70")
ip2 = ipaddress.ip_address("121.171.5.107")

mx = 0
for mask_len in range(32, -1, -1):
    net1 = ipaddress.ip_network(f"{ip1}/{mask_len}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{mask_len}", strict=False)

    if net1 == net2:
        mx = mask_len
        break

r = 2 ** (32 - mx)
print(r)
