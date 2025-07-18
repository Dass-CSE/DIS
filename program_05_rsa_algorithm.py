p, q = 13, 17
n = p * q
phi = (p-1)*(q-1)
e = 5
d = pow(e, -1, phi) #Modular inverse
msg = 10
cipher = pow(msg, e, n) #Encrypt
plain = pow(cipher, d, n) # Decrypt
print("Decrypted:", plain)
