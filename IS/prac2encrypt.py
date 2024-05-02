import math

def encrypt(plaintext, key):
    matrix = []
    cipher = ""
    kindex = 0

    msglen = len(plaintext)
    msglst = list(plaintext)
    keylist = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msglen / col))

    fillnull = int((row * col) - msglen)
    msglst.extend('_' * fillnull)

    for i in range(0, len(msglst), col):
        matrix.append(msglst[i:i + col])

    for j in range(col):
        currindex = key.index(keylist[kindex])
        cipher += ''.join([row[currindex] for row in matrix])
        kindex += 1

    return cipher

def decrypt(ciphertext, key):
    dec_cipher = []
    msg = ""
    k_indx = 0
    msg_indx = 0

    msg_len = float(len(ciphertext))
    msg_lst = list(ciphertext)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))

    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    msg = ''.join(sum(dec_cipher, []))
    return msg

plaintext = input("Enter plain text: ")
key = input("Enter key: ")

cipher = encrypt(plaintext, key)
print("Encrypted Message: {}".format(cipher))

ciphertext = input("Enter cipher text: ")
key = input("Enter key: ")

decrypted_message = decrypt(ciphertext, key)
print("Decrypted Message: {}".format(decrypted_message))
