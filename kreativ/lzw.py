def compress(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_code = ""

    for char in data:
        current_code += char
        if current_code not in dictionary:
            result.append(dictionary[current_code[:-1]])
            dictionary[current_code] = next_code
            next_code += 1
            current_code = char

    if current_code in dictionary:
        result.append(dictionary[current_code])

    return result

def decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = [chr(compressed_data[0])]
    current_code = chr(compressed_data[0])

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_code + current_code[0]
        else:
            raise ValueError("Bad compressed code")

        result.append(entry)
        dictionary[next_code] = current_code + entry[0]
        next_code += 1
        current_code = entry

    return ''.join(result)

# Contoh penggunaan
input_data = "Ilyasuas"

compressed_data = compress(input_data)
decompressed_data = decompress(compressed_data)

print("Input data:", input_data)
print("Compressed data:", compressed_data)
print("Decompressed data:", decompressed_data)
