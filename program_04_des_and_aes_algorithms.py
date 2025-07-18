from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes

# --- DES ---
des_key = get_random_bytes(8)
des = DES.new(des_key, DES.MODE_ECB)
msg = b"8ByteMsg"
cipher_des = des.encrypt(msg)
plain_des = des.decrypt(cipher_des)

# --- AES ---
aes_key = get_random_bytes(32)
aes = AES.new(aes_key, AES.MODE_ECB)
msg2 = b"16ByteMessage!!"
cipher_aes = aes.encrypt(msg2)
plain_aes = aes.decrypt(cipher_aes)

print("DES Decrypted:", plain_des)
print("AES Decrypted:", plain_aes)
