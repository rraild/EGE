import ipaddress

ip1 = ipaddress.ip_address("200.154.190.12")
ip2 = ipaddress.ip_address("200.154.184.0")

for mask_len in range(32, -1, -1):
    net1 = ipaddress.ip_network(f"{ip1}/{mask_len}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{mask_len}", strict=False)

    if net1 == net2:
        if ip1 != net1.network_address and ip1 != net1.broadcast_address:
            if ip2 != net1.network_address and ip2 != net1.broadcast_address:
                print(mask_len)
                break
