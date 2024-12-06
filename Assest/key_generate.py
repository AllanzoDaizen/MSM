from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
import os

class RSAkey:
    def __init__(self, username):
        self.private_key = None
        self.public_key = None
        self.username = username
        
    def generate_key(self):
        key = RSA.generate(2048)
        self.private_key = key.export_key().decode()
        self.public_key = key.publickey().export_key().decode()
        self.save_key()
    
    def save_key(self):
        # Example function to save keys, adjust to your needs
        folder_name = f"./Files/{self.username}"

        with open(f"{folder_name}/{self.username}private.pem", "w") as private_file:
            private_file.write(self.private_key)

        with open(f"{folder_name}/{self.username}public.pem", "w") as public_file:
            public_file.write(self.public_key)

