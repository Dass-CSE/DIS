import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES (?, ?)", ('admin', 'admin123'))

user_input = "' OR '1'='1"
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (user_input, user_input))

print("Logged in!" if cursor.fetchone() else "Login failed.")
