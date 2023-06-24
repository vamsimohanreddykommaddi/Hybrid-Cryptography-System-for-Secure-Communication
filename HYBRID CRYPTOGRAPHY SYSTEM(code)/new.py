from vigenere3 import *
from polybius3 import *

def hybrid_cipher(plaintext,key1,key2):
    fciphertext=polybius_encrypt(vigenere_encrypt(plaintext,key1),key2)
    return fciphertext

#plaintext=input()
#key1=input()
#key2=input()
#print(hybrid_cipher(plaintext,key1,key2))