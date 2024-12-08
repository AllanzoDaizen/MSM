from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Assest import key_generate
from Assest import create_folder
from Assest import usr_authen
from Assest import encrypt
import json
import hashlib
import socket
import threading

# def listen(client_socket):
#     try:
#         while True:
#             request=client_socket.recv(1024)
#             request=request.decode("utf-8")
#             if request == "exit":
#                 break
#             print(f"\nrecived mes: {request}")
#         client_socket.close()
        
#     except Exception as e:
#         print(e)
    
# def send_mes(peer):
#     try:
#         while True:
#             mes=input("\nenter message: ")
#             new_mes=mes.encode('utf-8')
#             if mes == "exit":
#                 break
#             peer.send(new_mes)
#         peer.close()
        
#     except Exception as e: 
#         print(e)
        
# def peer():
#     try:
#         peer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         peer.connect(("localhost",2000))
        
        
#         threading.Thread(target=listen,args=(peer,)).start()
#         threading.Thread(target=send_mes,args=(peer,)).start()
#     except Exception as e:
#         print(e)
        

def main(choices):
    if choices == 1:
        while True:
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
                    continue  
                else:
                    CreateFd = create_folder.Create_folder(username)
                    CreateFd.create_folder()
                    KeyGenerate = key_generate.RSAkey(username)
                    KeyGenerate.generate_key()
                    KeyGenerate.save_key()
                    print("Account created successfully!")
                    break  
            else:
                print("Passwords do not match. Please try again.\n")
                continue
    elif choices == 2:
        while True:
            print("-"*36)
            print("|         Login         |")
            print("-"*36)

            username = input("Username         : ")
            usr_pass = input("Password         : ")

            login = usr_authen.Usr_Create(username, usr_pass)
            if login.usr_login() == True:
                print("Login successfully!\n")
                while True:
                    print("-"*36)
                    print("|       Operation       |")
                    print("-"*36)
                    print("1. Message Encryption and Decryption\n2. File Encryption and Decryption\n3.Exit")
                    secondChoice = int(input("Enter a choice: "))

                    if secondChoice == 3:
                        break

                    elif secondChoice == 1:
                        while True:
                            print("-"*36)
                            print("|       Message       |")
                            print("-"*36)
                            print("1. Encryption\n2. Decryption\n3. Exit")   
                            thirdChoice = int(input("Enter a choice: "))

                            if thirdChoice == 3:
                                break

                            elif thirdChoice == 1:
                                message_encrypt = encrypt.Encryption(username)
                                message = input("Enter a message: ")
                                a=message_encrypt.encrypt_message(message)
                                print("mes: ",a)

                            elif thirdChoice == 2:
                                # message decrypt block
                                continue
                    elif secondChoice == 2:
                        while True:
                            print("-"*36)
                            print("|       File        |")
                            print("-"*36)
                            print("1. Encryption\n2. Decryption\n3. Exit")   
                            thirdChoice = int(input("Enter a choice: "))
                            if thirdChoice == 3:
                                break
                            elif thirdChoice == 1:
                                file_encrypt = encrypt.Encryption(username)
                                input_file = input("Enter a file path: ")
                                print(f"File path: {input_file} encrypted !")
                                output_file = input("Enter a path to save: ")
                                file_encrypt.encrypt_file(input_file, output_file)  
                            elif thirdChoice == 2:
                                # file decrypt block
                                continue      

                if secondChoice == 3:
                    break

            else:
                print("Login Failed!")

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
