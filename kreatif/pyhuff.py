import heapq
from collections import defaultdict

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0][1:]

def huffman_encoding(data):
    if not data:
        return None, None

    tree = build_huffman_tree(data)
    huffman_codes = {char: code for char, code in tree}
    encoded_data = ''.join(huffman_codes[char] for char in data)

    return encoded_data, tree

def huffman_decoding(encoded_data, tree):
    if not encoded_data or not tree:
        return None

    decoded_data = ""
    current = tree
    for bit in encoded_data:
        if bit == '0':
            current = current[0]
        else:
            current = current[1]

        if type(current[0]) is str:
            decoded_data += current[0]
            current = tree

    return decoded_data

# Contoh penggunaan
input_data = "uasilyas"

encoded_data, huffman_tree = huffman_encoding(input_data)
decoded_data = huffman_decoding(encoded_data, huffman_tree)

print("Input data:", input_data)
print("Huffman Tree:", huffman_tree)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
