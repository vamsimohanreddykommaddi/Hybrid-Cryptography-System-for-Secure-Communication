import string

def generate_polybius_key(key):
    alphabet = string.ascii_lowercase
    # Remove any duplicate characters from the keyword
    key = "".join(sorted(set(key.lower())))
    # Remove the keyword letters from the alphabet
    alphabet = alphabet.translate(str.maketrans("", "", key))
    # Construct the Polybius square key
    polybius_key = key + alphabet
    return polybius_key

def polybius_encrypt(plaintext, key):
    # Generate the Polybius square key
    polybius_key = generate_polybius_key(key)
    # Create a dictionary mapping characters to their Polybius square coordinates
    polybius_dict = {}
    for i in range(len(polybius_key)):
        row = i // 5 + 1
        col = i % 5 + 1
        polybius_dict[polybius_key[i]] = (row, col)
    # Encrypt the plaintext message
    ciphertext = ""
    for char in plaintext.lower():
        if char == " ":
            ciphertext += " "
        elif char in polybius_key:
            row, col = polybius_dict[char]
            ciphertext += str(row) + str(col)
    return ciphertext

def polybius_decrypt(ciphertext, key):
    # Generate the Polybius square key
    polybius_key = generate_polybius_key(key)
    # Create a dictionary mapping Polybius square coordinates to characters
    polybius_dict = {}
    for i in range(len(polybius_key)):
        row = i // 5 + 1
        col = i % 5 + 1
        polybius_dict[(row, col)] = polybius_key[i]
    # Decrypt the ciphertext message
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == " ":
            plaintext += " "
            i += 1
        else:
            row = int(ciphertext[i])
            col = int(ciphertext[i+1])
            char = polybius_dict[(row, col)]
            plaintext += char
            i += 2
    return plaintext

#print(polybius_encrypt('ltz owiqx owuf lzs pztr','mate'))
#print(polybius_decrypt('341461 4153314354 41535123 346145 42611444','mate'))