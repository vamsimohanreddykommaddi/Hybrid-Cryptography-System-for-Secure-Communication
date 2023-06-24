import string

def vigenere_encrypt(plaintext, key):
    # Convert the plaintext and key to lowercase
    plaintext = plaintext.lower()
    key = key.lower()
    # Create a list of characters that should not be encrypted
    preserve_chars = string.digits + string.punctuation + " "
    # Encrypt the plaintext message
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char in preserve_chars:
            ciphertext += char
        else:
            # Shift the character by the corresponding amount in the key
            shift = ord(key[key_index]) - ord('a')
            char_shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += char_shifted
            key_index = (key_index + 1) % len(key)
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    # Convert the ciphertext and key to lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()
    # Create a list of characters that should not be decrypted
    preserve_chars = string.digits + string.punctuation + " "
    # Decrypt the ciphertext message
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char in preserve_chars:
            plaintext += char
        else:
            # Shift the character back by the corresponding amount in the key
            shift = ord(key[key_index]) - ord('a')
            char_shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += char_shifted
            key_index = (key_index + 1) % len(key)
    return plaintext
