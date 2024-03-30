"""Crypt converting"""

def crypt(codes, data):
    """Crypt data"""
    result = ''

    for letter in data:
        result += codes[letter]

    bits = len(result)
    result = result + '0'*(8-(len(result)%8))
    output_bytes = bytearray([int(result[i*8:i*8+8],2) for i in range(int(len(result)/8))])

    return [output_bytes, bits]

def encrypt(codes, data):
    """Encrypt data"""
    read_data = ''.join(['{:0>8}'.format(str(bin(item))[2:]) for item in data])
    result = ''

    while read_data:
        size_before = len(read_data)

        for k, v in codes.items():
            if read_data[0:len(v)] == v:
                result += k
                read_data = read_data[len(v):len(read_data)]

        if size_before == len(read_data):
            break

    return result
