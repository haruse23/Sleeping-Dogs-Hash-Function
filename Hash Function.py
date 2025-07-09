import struct

# Load the table
with open(r"Hash Function Lookup Table.bin", "rb") as f:
    data = f.read()

# Convert 1024 bytes into 256 little-endian 32-bit integers
table = list(struct.unpack("<256I", data))

# Now you can use it in your custom hash function
def custom_hash(s, seed=0xFFFFFFFF):
    h = seed
    for c in s:
        c = ord(c)
        if 0x61 <= c <= 0x7A:  # a-z
            c -= 0x20
        index = ((h >> 24) ^ c) & 0xFF
        h = ((h << 8) & 0xFFFFFFFF) ^ table[index]
    return h

# Example
print(hex(custom_hash("")))
