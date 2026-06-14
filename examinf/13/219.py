node_byte = 52
net_byte = 0

p = [0, 128, 192, 224, 240, 248, 252, 254, 255]
valid_masks = []

for m in p:
    if (node_byte & m) == net_byte:
        valid_masks.append(m)

print(max(valid_masks))
