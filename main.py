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
            if len(username) < 3:
                print("Username must be at least 2 characters long.")
                continue
            else:
                email = input("Email\t\t : ")
                if email.strip() == "":
                    print("Email cannot be empty.")
                    continue
                usr_pass = getpass.getpass("Password\t : ")
                if len(usr_pass) < 8:
                    print("Password must be at least 8 characters long.")
                    continue
                else:
                    if not (any(char.isdigit() for char in usr_pass) and
                            any(char.isupper() for char in usr_pass) and
                            any(char.islower() for char in usr_pass) and
                            any(char in "!@#$%^&*()_+" for char in usr_pass)):
                        print("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                        continue
                    else:
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
            print("-" * 36)
            print("|\t\tLogin\t\t   |")
            print("-" * 36)

            username = input("Username         : ")
            usr_pass = getpass.getpass("Password         : ")

            try:
                login = usr_authen.Usr_Create(username, usr_pass, email=None)
                if login.usr_login():
                    print("Login successfully!\n")
                    while True:
                        print("-" * 36)
                        print("|\t      Operation\t\t   |")
                        print("-" * 36)
                        print("1. Message Encryption and Decryption\n2. File Encryption and Decryption\n3. Secret Chat\n4. Exit")
                        try:
                            secondChoice = int(input("Enter a choice: "))
                            if secondChoice == 4:
                                break

                            elif secondChoice == 1:
                                while True:
                                    print("-" * 36)
                                    print("|\t     Message\t\t   |")
                                    print("-" * 36)
                                    print("1. Encryption\n2. Decryption\n3. Exit")   
                                    try:
                                        thirdChoice = int(input("Enter a choice: "))
                                        if thirdChoice == 3:
                                            break

                                        elif thirdChoice == 1:
                                            message_encrypt = encrypt.Encryption(username)
                                            message = input("Enter a message: ")

                                            if not message.strip():
                                                print("Error: Message cannot be empty.")
                                            else:
                                                mess_encrypted = message_encrypt.encrypt_message(message)
                                                print("Message encrypted: {0}".format(mess_encrypted))

                                        elif thirdChoice == 2:
                                            message_decrypt = decrypt.Decryption(username)
                                            message = input("Enter a message: ")

                                            if not message.strip():
                                                print("Message cannot be empty.")
                                            else:
                                                mess_decrypt = message_decrypt.decrypt_message(message)
                                                print("Message decrypted: {0}".format(mess_decrypt))
                                        else:
                                            print("Please enter a number (1-3).")
                                    except ValueError:
                                        print("Error: Invalid input. Please enter a number (1-3).")
                                    except Exception as e:
                                        print(f"An error occurred: {e}")

                            elif secondChoice == 2:
                                while True:
                                    print("-" * 36)
                                    print("|\t\tFile\t\t   |")
                                    print("-" * 36)
                                    print("1. Encryption\n2. Decryption\n3. Exit")   
                                    try:
                                        thirdChoice = int(input("Enter a choice: "))
                                        if thirdChoice == 3:
                                            break
                                        elif thirdChoice == 1:
                                            file_encrypt = encrypt.Encryption(username)
                                            input_file = input("Enter a file path: ")
                                            if not input_file.strip():
                                                print("Path of file cannot be empty!")
                                            else:
                                                output_file = input("Enter a path to save: ")
                                                if not output_file.strip():
                                                    print("Path to save file cannot be empty!")
                                                else:
                                                    file_encrypt.encrypt_file(input_file, output_file) 

                                        elif thirdChoice == 2:
                                            file_decrypt = decrypt.Decryption(username)
                                            input_file = input("Enter a file path: ")
                                            if not input_file.strip():
                                                print("Path of file cannot be empty!")
                                            else:
                                                output_file = input("Enter a path to save: ")
                                                if not output_file.strip():
                                                    print("Path to save file cannot be empty!")
                                                else:
                                                    file_decrypt.decrypt_file(input_file, output_file)
                                        else:
                                            print("Please enter a number (1-3).")
                                    except ValueError:
                                        print("Error: Invalid input. Please enter a number (1-3).")
                                    except Exception as e:
                                        print(f"An error occurred: {e}")

                            elif secondChoice == 3:
                                print("-" * 36)
                                targ_name = input("Target's username: ")
                                try:
                                    secret_user.peer(username, targ_name)
                                except Exception as e:
                                    print(f"Error establishing secret chat: {e}")
                            else:
                                print("Error: Invalid choice. Please select 1-4.")

                        except ValueError:
                            print("Error: Invalid input. Please enter a number (1-4).")

                    break
                else:
                    print("Login Failed!")
                    i -= 1

                if i == 0:
                    print("Access denied!")
                    print("Forgot password?")
                    try:
                        back = int(input("Enter 1 to go back: "))
                        if back == 1:
                            break
                    except ValueError:
                        print("Error: Invalid input. Returning to main menu.")
            except Exception as e:
                print(f"An error occurred during login: {e}")

    elif choices == 3:
        while True:
            print("-" * 36)
            print("|\t  Password Recovery\t   |")
            print("-" * 36)
            username = input("Username\t\t: ")
            email = input("Email\t\t\t: ")
            try:
                recovery = usr_authen.pass_recover()
                if recovery.check_email(username, email):
                    usr_newpass = getpass.getpass("New password\t\t:")
                    usr_confirm_new_pass = getpass.getpass("Confirm password\t: ")
                    if usr_newpass == usr_confirm_new_pass:
                        if recovery.change_pass(username, usr_newpass):
                            print("Password changed successfully!")
                            break
                        else:
                            print("Error: Password change failed.")
                    else:
                        print("Passwords do not match! Try again!")
                else:
                    print("Error: Username or Email incorrect! Try again!")
            except Exception as e:
                print(f"An error occurred during password recovery: {e}")

if __name__ == "__main__":
    while True:
        print("-" * 25)
        print("|\tSecureOps\t|")
        print("-" * 25)
        print("1. Create Account\n2. Login\n3. Forget Password\n4. Exit")
        try:
            ch = int(input("Enter a choice: "))
            if ch == 4:
                print("Exiting the program. Goodbye!")
                break
            elif 1 <= ch <= 3:
                main(ch)
            else:
                print("Error: Please enter a valid choice (1-4).")
        except ValueError:
            print("Error: Invalid input. Please enter a number (1-4).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
