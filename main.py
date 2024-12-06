from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Assest import key_generate
from Assest import create_folder
from Assest import usr_authen
import json
import hashlib

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
    # elif choices == 2:
        #after login it will be 

if __name__ == "__main__":
    while True:
        print("-"*36)
        print("|   MNF Encryption and Decryption   |")
        print("-"*36)
        print("1. Create Account\n2. Login\n3. Exit")
        ch = int(input("Enter a choice: "))
        if ch == 3:
            break
        else:
            main(ch)
