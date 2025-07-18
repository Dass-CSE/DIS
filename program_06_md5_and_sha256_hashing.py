import hashlib

text = "hello world"
md5_hash = hashlib.md5(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print("Input       :", text)
print("MD5 Hash    :", md5_hash)
print("SHA-256 Hash:", sha256_hash)
