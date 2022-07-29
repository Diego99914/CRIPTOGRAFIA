def xor_data(binary_data_1, binary_data_2):
    return bytes([b1^b2 for b1,b2 in zip (binary_data_1, binary_data_2)])

k1 = bytes.fromhex('B98A15BA31AEBB22')
k2 = bytes.fromhex('A1EF2ABFE1AAEEFF')

print(xor_data(k1,k2).hex())