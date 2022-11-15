import string

plaintext = 'SELAMAT DATANG DI KELAS KRIPTOGRAFI'
a = 17
b = 3

def encrypt(plaintext,a,b):
    ciphertext = ''
    for p in plaintext:
        if p == ' ': c = ' '
        else:
            index_p = string.ascii_uppercase.index(p) 
            c = string.ascii_uppercase[(index_p * a + b)%26]
        ciphertext += c
    return ciphertext

ciphertext = encrypt(plaintext,a,b)
print(ciphertext)
