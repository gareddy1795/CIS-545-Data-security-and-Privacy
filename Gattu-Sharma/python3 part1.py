import base64

def encode(text):
    return base64.b64encode(text)

def decode(text):
    return base64.b64decode(text)

def encrypt(cleartext, key):
    cipher = bytearray(len(cleartext))
    for i in range(len(cleartext)):
        cipher[i] = 0 ^ ord(cleartext[i]) ^ key
    return cipher

def decrypt(ciphertext, key):
    # Decrypt the ciphertext using the provided key.
    cleartext = ''
    for i in range(len(ciphertext)):
        cleartext += chr(0 ^ ciphertext[i] ^ key)
    return cleartext

def main():
    cipher_text = "XWJkYzd1cnR2YmRyN254YjdyeXRlbmdjcnM3djdkcnRlcmM3c3hyZHkwYzd6dnxyN35jN2RydGJlcjY="
    cipher_text_bytes = decode(cipher_text)

    for candidate_key in range(256):
        candidate_cleartext = decrypt(cipher_text_bytes, candidate_key)
        if all(32 <= ord(char) <= 126 for char in candidate_cleartext):
            print(f"Key found: {candidate_key}")
            print(f"Decrypted text: {candidate_cleartext}")

if __name__ == '__main__':
    main()
