om Code import encrypt, decrypt, usr_authen, key_generate, create_folder, secret_user
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
