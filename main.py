from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Code import encrypt, decrypt, usr_authen, key_generate, create_folder, secret_user
import getpass
import json
import hashlib

def main(choices):
    if choices == 1:
        while True:
            print("-"*36)
            print("|\t   Create account\t   |")
            print("-"*36)

            username = input("Username\t : ")
            email = input("Email\t\t : ")
            usr_pass = getpass.getpass("Password\t : ")
            usr_verifypass = getpass.getpass("Confirm password : ")

            if usr_pass == usr_verifypass:
                authen = usr_authen.Usr_Create(username, usr_pass, email)
                if authen.usr_pass() == False:
                    print("Try Again!\n")
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
        i = 3
        while i > 0:
            print("-"*36)
            print("|\t\tLogin\t\t   |")
            print("-"*36)

            username = input("Username         : ")
            usr_pass = input("Password         : ")

            login = usr_authen.Usr_Create(username, usr_pass, email=None)
            
            if login.usr_login() == True:
                print("Login successfully!\n")
                while True:
                    print("-"*36)
                    print("|\t      Operation\t\t   |")
                    print("-"*36)
                    print("1. Message Encryption and Decryption\n2. File Encryption and Decryption\n3. Secret Chat\n4. Exit")
                    secondChoice = int(input("Enter a choice: "))

                    if secondChoice == 4:
                        break

                    elif secondChoice == 1:
                        while True:
                            print("-"*36)
                            print("|\t     Message\t\t   |")
                            print("-"*36)
                            print("1. Encryption\n2. Decryption\n3. Exit")   
                            thirdChoice = int(input("Enter a choice: "))

                            if thirdChoice == 3:
                                break

                            elif thirdChoice == 1:
                                message_encrypt = encrypt.Encryption(username)
                                message = input("Enter a message: ")
                                mess_encrypted = message_encrypt.encrypt_message(message)
                                print("Message encrypted: {0}".format(mess_encrypted))

                            elif thirdChoice == 2:
                                message_decrypt = decrypt.Decryption(username)
                                message = input("Enter a message: ")
                                mess_decrypt = message_decrypt.decrypt_message(message)
                                print("Message decrypted: {0}".format(mess_decrypt))


                    elif secondChoice == 2:
                        while True:
                            print("-"*36)
                            print("|\t\tFile\t\t   |")
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
                                file_decrypt = decrypt.Decryption(username)
                                input_file = input("Enter a file path: ")
                                print(f"File path: {input_file} decrypted !")
                                output_file = input("Enter a path to save: ")
                                file_decrypt.decrypt_file(input_file, output_file) 
                    elif secondChoice == 3:
                        print("-"*36)
                        targ_name = input("Target's username: ")
                        secret_user.peer(username, targ_name)
                        
                break  
                
            else:
                print("Login Failed!")
                i -= 1

            if i == 0:
                print("Forgot password?")
                back = int(input("Enter 1 to go back: "))
                if back == 1:
                    break

    elif choices == 3:
        while True:
            print("-"*36)
            print("|\t  Password Recovery\t   |")
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
