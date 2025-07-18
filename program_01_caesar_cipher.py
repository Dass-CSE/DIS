text = "HELLO"
key = 3
enc = "".join([chr((ord(c)-65+key)%26+65) for c in text])  # Encrypt
dec = "".join([chr((ord(c)-65-key)%26+65) for c in enc])    # Decrypt
print("Encrypted:", enc)
print("Decrypted:", dec)
