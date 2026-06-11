import ipaddress

node_ip = "69.121.128.142"
mask = "255.255.252.0"

net = ipaddress.ip_network(f"{node_ip}/{mask}", strict=False)

max_host = max(net.hosts())

print("".join(str(max_host).split(".")))
