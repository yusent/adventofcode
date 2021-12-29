from math import prod

def hex_to_bin(h):
    return format(int(h, 16), "b").zfill(len(h) * 4)

def parse(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    value, rem = None, None

    if type_id == 4:
        value, rem = parse_literal(bits[6:])
        value = int(value, 2)
    elif bits[6] == "0":
        length = int(bits[7:22], 2)
        value, rem = parse_sub_packets(bits[22:22+length]), bits[22+length:]
    else:
        length = int(bits[7:18], 2)
        value, rem = parse_n_sub_packets(bits[18:], length)

    return { "ver": version, "type": type_id, "val": value }, rem

def parse_literal(bits):
    if bits[0] == "0":
        return bits[1:5], bits[5:]

    next_bits, rem = parse_literal(bits[5:])
    return f"{bits[1:5]}{next_bits}", rem

def parse_sub_packets(bits):
    if bits == "":
        return []

    packet, rem = parse(bits)
    return [packet, *parse_sub_packets(rem)]

def parse_n_sub_packets(bits, n):
    if n == 0:
        return [], bits

    packet, rem = parse(bits)
    packets, rem = parse_n_sub_packets(rem, n - 1)
    return [packet, *packets], rem

def sum_versions(packet):
    if packet["type"] == 4:
        return packet["ver"]

    return packet["ver"] + sum(sum_versions(p) for p in packet["val"])

def value(packet):
    if packet["type"] == 0:
        return sum(value(p) for p in packet["val"])
    if packet["type"] == 1:
        return prod(value(p) for p in packet["val"])
    if packet["type"] == 2:
        return min(value(p) for p in packet["val"])
    if packet["type"] == 3:
        return max(value(p) for p in packet["val"])
    if packet["type"] == 4:
        return packet["val"]
    if packet["type"] == 5:
        return int(value(packet["val"][0]) > value(packet["val"][1]))
    if packet["type"] == 6:
        return int(value(packet["val"][0]) < value(packet["val"][1]))
    if packet["type"] == 7:
        return int(value(packet["val"][0]) == value(packet["val"][1]))

if __name__ == "__main__":
    packet, _ = parse(hex_to_bin(open("input/day16").read().strip()))
    print("Part 1:", sum_versions(packet))
    print("Part 2:", value(packet))
