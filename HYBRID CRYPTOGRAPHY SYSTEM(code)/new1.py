from vigenere3 import *
from polybius3 import *

def hybrid_decipher(ciphertext,key1,key2):
    plaintext=vigenere_decrypt(polybius_decrypt(ciphertext,key2),key1)
    return plaintext

#ciphertext=input()
#key1=input()
#key2=input()
#print(hybrid_decipher(ciphertext,key1,key2))