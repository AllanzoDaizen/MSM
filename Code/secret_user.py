import hashlib
import socket
import threading
from Code import encrypt, decrypt

def listen(peer, username):
    try:
        while True:
            message_decrypt = decrypt.Decryption(username)
            request = peer.recv(4096)
            request = request.decode('utf-8')
            if not request:
                continue
            else:
                mess_decrypt = message_decrypt.decrypt_message(request)
                print(f"->{mess_decrypt}")
            if request.lower() == "exit":
                print("Connection closed by peer.")
                break
        peer.close()
    except Exception as e:
        print(f"Error in listening: {e}")
        pass

def send_mes(peer, username):
    try:
        while True:
            message_encrypt = encrypt.Encryption(username)
            message = input("")
            mes = message_encrypt.encrypt_message(message).encode('utf-8')
            if message.lower() == "exit":
                print("Exiting...")
                peer.send(mes)
                break
            if not message:
                print("Cannot send an empty message!")
                continue
            peer.send(mes)
        peer.close()
    except Exception as e:
        print(f"Error in sending: {e}")
        pass

def peer(username, targ_name):
    try:
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        role = int(input("Who are you?\n1. First Person(server)\n2. Second Person(client)\nEnter a choice: "))

        if role == 1:
            peer_ip = "localhost"
            peer_port = 2000
            peer.bind((peer_ip, peer_port))
            peer.listen(1)
            print("Waiting for connection...")
            client_socket, client_add = peer.accept()
            print(f"Connected with {client_add}")
            peer = client_socket
        elif role == 2:
            peer.connect(("localhost", 2000))
            print("Connected to the server.")
        else:
            print("Invalid role! Exiting...")
            return

        # Start listening and sending threads
        listen_thread = threading.Thread(target=listen, args=(peer, username,))
        send_thread = threading.Thread(target=send_mes, args=(peer, targ_name,))

        listen_thread.start()
        send_thread.start()

        listen_thread.join()
        send_thread.join()
    except Exception as e:
        print(f"Error in peer setup: {e}")

