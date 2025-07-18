text, key = "HELLO", "KEY"
key = (key * (len(text)//len(key)+1))[:len(text)]
enc = "".join([chr((ord(t)+ord(k)-2*65)%26+65) for t,k in zip(text,key)])
dec = "".join([chr((ord(e)-ord(k)+26)%26+65) for e,k in zip(enc,key)])
print("Encrypted:", enc)
print("Decrypted:", dec)
