def generateChar():
    charList = []
    for i in range(32, 127):
        # print(chr(i),end=" ")
        charList.append(str(chr(i)))
    return charList


# print(generateChar())

# all char to  compress with decimal
# main data
mainData = 'Han Zaw @+"'
b = 1
# for a in generateChar():
for a in mainData:
    decimal = ord(a)
    b <<= 7
    b |= decimal
    # print("main bit : ",bin(b))
    # print("Decimal :",bin(decimal))

print("binary value : ", bin(b))

from sys import getsizeof

# print(f"Original Size : {getsizeof(''.join(generateChar()))} Bytes")
# print(f'Compressed Size : {getsizeof(b)} Bytes')


gene: str = ""
for i in range(0, b.bit_length() - 1, 7):
    print(i)# - 1 to exclude         sentinel
    bits: int = b >> i & 0b1111111
    gene += chr(bits)
    # print(bin(bits))

print(f'Original Data : {mainData}')
print(f"Original Size : {getsizeof(mainData)} Bytes")
print(f'Compressed Size : {getsizeof(b)} Bytes')
print('\n')
print(f'DeCompressed Size : {getsizeof(gene[::-1])} Bytes')
print(f'Decompress Data :{gene[::-1]}')
