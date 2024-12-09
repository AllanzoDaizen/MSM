from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from Code import encrypt, decrypt, usr_authen, key_generate, create_folder
import json
import hashlib
import socket
import threading


def listen(client_socket,username):
    try:
        while True:
            message_decrypt = decrypt.Decryption(username)
            request=client_socket.recv(4096)
            request = request.decode('utf-8')
            if not request:
                continue
            else:
                # print(f"\nrecived mes: {request}\n")
                message_decrypt.decrypt_message(request)
            if request == "exit":
                break
        client_socket.close()
        
    except Exception as e:
        print(e)
    
def send_mes(peer,username):
    try:
        while True:
            message_encrypt = encrypt.Encryption(username)
            message = input(" ")
            mes=message_encrypt.encrypt_message(message)
            mes = mes.encode('utf-8')
            if message == "exit":
                break
            if not message:
                continue
            peer.send(mes)
        peer.close()
        
    except Exception as e: 
        print(e)
        
def peer(username,targ_name):
    try:
        peer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        peer_ip="localhost"
        peer_port=2000
        peer.bind((peer_ip,peer_port))
        peer.listen(1)
        client_socket,client_add=peer.accept()
        print(f"the device is connected with {client_add}")
        peer=client_socket
        
        listen_thread=threading.Thread(target=listen,args=(peer,username,))
        send_thread=threading.Thread(target=send_mes,args=(peer,targ_name,))
        
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
            email = input("Email            : ")
            usr_pass = input("Password         : ")
            usr_verifypass = input("Confirm password : ")

            if usr_pass == usr_verifypass:
                authen = usr_authen.Usr_Create(username, usr_pass, email)
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
            
            print("-"*36)
            targ_name=input("target_username: ")

            login = usr_authen.Usr_Create(username, usr_pass,email=None)
            if login.usr_login() == True:
                print("Login successfully!\n")
                peer(username,targ_name)
                
    elif choices == 3:
        while True:
            print("-"*36)
            print("|       Password Recovery       |")
            print("-"*36)
            username = input("Username: ")
            email = input("Email: ")
            recovery = usr_authen.pass_recover()
            if recovery.check_email(username, email) == True:
                usr_newpass = input("New password:")
                usr_confirm_new_pass = input("Confirm new password: ")
                if usr_newpass == usr_confirm_new_pass:
                    
                    if recovery.change_pass(username, usr_newpass) == True:
                        print("Password changed successfully!")
                        break
                    else:
                        print("Password cannot change! Try again!")
                
                
if __name__ == "__main__":
    while True:
        print("-"*36)
        print("|   MNF Encryption and Decryption   |")
        print("-"*36)
        print("1. Create Account\n2. Login\n3. Forget Password\n4. Exit")
        ch = int(input("Enter a choice: "))
        if ch == 4:
            break
        else:
            main(ch)