input_string = input("Enter a string: ")
result=[]
result1=[]
for char in input_string:
    a = ord(char)
    b = 127
    k = a & b
    j = a ^ b
    result.append(chr(k))
    result1.append(chr(j))
    print("Converted value of", char, "in AND is:", bin(k)[2:], "and:",k,"and:",chr(k))
    print("Converted value of", char, "in XOR is:", bin(j)[2:],"and:",j, "and:",chr(j))

print(result)
print(result1)

"""
RSA extra
P, Q, M = 3, 11, 3
n = P * Q
phi = (P - 1) * (Q - 1)
e, d = 3, pow(3, -1, phi)
C = pow(M, e, n)
decrypted_message = pow(C, d, n)

print("Encrypted message (C):", C)
print("Decrypted message:", decrypted_message)
"""
