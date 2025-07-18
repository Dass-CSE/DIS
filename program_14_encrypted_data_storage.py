from cryptography.fernet import Fernet
import sqlite3

key = Fernet.generate_key()
fernet = Fernet(key)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (name TEXT, password TEXT)")

plain_password = "my_secret_pwd"
enc_password = fernet.encrypt(plain_password.encode()).decode()

cursor.execute("INSERT INTO users VALUES (?, ?)", ("admin", enc_password))

cursor.execute("SELECT password FROM users WHERE name=?", ("admin",))
enc_pwd_from_db = cursor.fetchone()[0]
dec_password = fernet.decrypt(enc_pwd_from_db.encode()).decode()

print("Decrypted Password:", dec_password)
