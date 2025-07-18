import socket
import threading
import time

def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

key = 123

def run_server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    print("[Server] Listening on port 5000...")
    conn, addr = server_socket.accept()
    print(f"[Server] Connected to: {addr}")
    encrypted_data = conn.recv(1024)
    decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
    print("[Server] Decrypted message from client:", decrypted_data.decode())
    response = "Hello Secure Client!".encode()
    encrypted_response = xor_encrypt_decrypt(response, key)
    conn.send(encrypted_response)
    conn.close()
    server_socket.close()

def run_client():
    time.sleep(1)
    client_socket = socket.socket()
    client_socket.connect(('localhost', 5000))
    print("[Client] Connected to server.")
    message = "Hello Secure Server!".encode()
    encrypted_message = xor_encrypt_decrypt(message, key)
    client_socket.send(encrypted_message)
    encrypted_reply = client_socket.recv(1024)
    reply = xor_encrypt_decrypt(encrypted_reply, key)
    print("[Client] Decrypted message from server:", reply.decode())
    client_socket.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    run_client()
    server_thread.join()
