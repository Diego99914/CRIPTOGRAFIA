def xor_data(binary_data_1, binary_data_2):
    return bytes([b1^b2 for b1,b2 in zip (binary_data_1, binary_data_2)])

k2 = bytes.fromhex('A1EF2ABFE1AAEEFF')
k = bytes.fromhex('B1AA12BA21AABB12')


print(xor_data(k,k2).hex())