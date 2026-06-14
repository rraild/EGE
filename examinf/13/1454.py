import ipaddress

net = ipaddress.ip_network("210.189.23.15/255.255.248.0", strict=False)

min_ip = net.network_address

octs = str(min_ip).split(".")
print("".join(octs))
