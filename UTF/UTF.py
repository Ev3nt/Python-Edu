def Crypt(codes, data):
    result = ''

    for letter in data:
        result += codes[letter]

    bits = len(result)
    result = result + '0'*(8-(len(result)%8))
    outputBytes = bytearray([int(result[i*8:i*8+8],2) for i in range(int(len(result)/8))])

    return [outputBytes, bits]

def Decrypt(codes, data):
    readData = ''.join(['{:0>8}'.format(str(bin(item))[2:]) for item in data])
    result = ''

    while len(readData):
        sizeBefore = len(readData)

        for k, v in codes.items():
            if readData[0:len(v)] == v:
                result += k
                readData = readData[len(v):len(readData)]

        if sizeBefore == len(readData):
            break

    return result