from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Code import encrypt, decrypt, usr_authen, key_generate, create_folder
import json
import hashlib
import socket
import threading


def listen(client_socket):
    try:
        while True:
            request=client_socket.recv(4096)
            request=request.decode("utf-8")
            if request == "exit":
                break
            print(f"\nrecived mes: {request}")
        client_socket.close()
        
    except Exception as e:
        print(e)
    
def send_mes(peer,message_encrypt):
    try:
        while True:
            message = input("Enter a message: ")
            mes=message_encrypt.encrypt_message(message)
            new_mes=mes.encode('utf-8')
            if message == "exit":
                break
            if not message:
                continue
            peer.send(new_mes)
        peer.close()
        
    except Exception as e: 
        print(e)
        
def peer(message_encrpyt):
    try:
        peer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        peer.connect(("localhost",2000))
        
        
        listen_thread=threading.Thread(target=listen,args=(peer,))
        send_thread=threading.Thread(target=send_mes,args=(peer,message_encrpyt,))
        
        listen_thread.start()
        send_thread.start()
        
        listen_thread.join()  
        send_thread.join()
    except Exception as e:
        print(e)
        

def main(choices):
    if choices == 1:
        print("-"*36)
        print("|         Create account         |")
        print("-"*36)

        username = input("Username         : ")
        usr_pass = input("Password         : ")
        usr_verifypass = input("Confirm password : ")

        if usr_pass == usr_verifypass:
            authen = usr_authen.Usr_Create(username, usr_pass)
            if authen.usr_pass() == False:
                print("Try Again!!\n")
     
            else:
                CreateFd = create_folder.Create_folder(username)
                CreateFd.create_folder()
                KeyGenerate = key_generate.RSAkey(username)
                KeyGenerate.generate_key()
                KeyGenerate.save_key()
                print("Account created successfully!")
 
        else:
            print("Passwords do not match. Please try again.\n")
            
    elif choices == 2:
            print("-"*36)
            print("|         Login         |")
            print("-"*36)

            username = input("Username         : ")
            usr_pass = input("Password         : ")

            login = usr_authen.Usr_Create(username, usr_pass)
            if login.usr_login() == True:
                print("Login successfully!\n")
                message_encrypt = encrypt.Encryption(username)
                peer(message_encrypt)
                
                
if __name__ == "__main__":
    while True:
        print("-"*36)
        print("|   MNF Encryption and Decryption   |")
        print("-"*36)
        print("1. Create Account\n2. Login\n3. Forget Password\n4. Forget Key\n5. Exit")
        ch = int(input("Enter a choice: "))
        if ch == 5:
            break
        else:
            main(ch)