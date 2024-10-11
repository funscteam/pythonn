def shannon_fano(data):
    if len(data) == 1:
        return {data[0]: '0'}

    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    total_frequency = sum([freq for _, freq in sorted_data])
    cumulative_frequency = 0

    for i in range(len(sorted_data)):
        cumulative_frequency += sorted_data[i][1]
        if cumulative_frequency >= total_frequency / 2:
            break

    group1 = dict(sorted_data[:i + 1])
    group2 = dict(sorted_data[i + 1:])

    code = {}
    for char, freq in group1.items():
        code[char] = '0' + code.get(char, '')

    for char, freq in group2.items():
        code[char] = '1' + code.get(char, '')

    if len(group1) > 1:
        code.update(shannon_fano(group1))

    if len(group2) > 1:
        code.update(shannon_fano(group2))

    return code

# Contoh penggunaan
input_data = "ilyasuas"
frequency_dict = {char: input_data.count(char) for char in set(input_data)}

shannon_fano_code = shannon_fano(frequency_dict)

encoded_data = ''.join(shannon_fano_code[char] for char in input_data)
decoded_data = ""

for code in shannon_fano_code:
    index = 0
    while index != len(encoded_data):
        if encoded_data.startswith(shannon_fano_code[code], index):
            decoded_data += code
            index += len(shannon_fano_code[code])
        else:
            break

print("Input data:", input_data)
print("Shannon-Fano Code:", shannon_fano_code)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
