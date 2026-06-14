import ipaddress

net = ipaddress.ip_network("83.152.68.115/255.255.224.0", strict=False)
max_host = max(net.hosts())

print("".join(str(max_host).split(".")))
