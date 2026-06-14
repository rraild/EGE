import ipaddress

net = ipaddress.ip_network("115.15.60.15/255.255.128.0", strict=False)

max_ip = net.broadcast_address

octs = str(max_ip).split(".")
print("".join(octs))
