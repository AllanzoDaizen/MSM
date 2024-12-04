from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Assest import key_generate
from Assest import create_folder
# Prompt for input
usr_name = input("Username: ")

try:
    folder_obj = create_folder.Create_folder(usr_name)
    # Create an instance of RSAkey with input
    key_obj = key_generate.RSAkey(usr_name)

    # Create folder for the user
    folder_obj.create_folder()

    # Generate RSA keys
    key_obj.generate_key()

    print("Key object created and key generation successful!")

except Exception as e:
    print(f"An error occurred: {e}")