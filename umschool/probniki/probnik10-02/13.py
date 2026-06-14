import ipaddress

ip = "116.109.66.45"
net = "116.109.64.0"

for mask in range(33):
    network = ipaddress.ip_network(f"{ip}/{mask}", strict=False)
    if str(network.network_address) == net:
        print(network.netmask)
