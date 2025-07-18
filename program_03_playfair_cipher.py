from pycipher import Playfair
pf = Playfair('KEYWORD')  # Create cipher with keyword
enc = pf.encipher('HELXLO')  # X used for repeating letters
dec = pf.decipher(enc)
print("Encrypted:", enc)
print("Decrypted:", dec)
