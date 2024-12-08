import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from base64 import b64encode
class Encryption:
    def __init__(self, username):
        self.username = username
    def encrypt_message(self, message):
        try:
            public_key_path = f"./Files/{self. username}/{self.username}public.pem"
            # Load the public key from the file
            with open(public_key_path, "rb") as public_file:
                public_key = serialization.load_pem_public_key(public_file.read())

            # Encrypt the message
            encrypted_message = public_key.encrypt(
                message.encode(),  # Convert the message to bytes
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=SHA256()),  # Mask Generation Function
                    algorithm=SHA256(),  # Hashing algorithm
                    label=None
                )
            )

            # Encode the encrypted message as Base64 for easier storage/display
            return b64encode(encrypted_message).decode()

        except Exception as e:
            print(f"Error encrypting message: {e}")
            return None

    def encrypt_file(self, input_file_path, output_file_path):
        try:
            # Load the public key from the file
            public_key_path = f"./Files/{self. username}/{self.username}public.pem"

            with open(public_key_path, "rb") as public_file:
                public_key = serialization.load_pem_public_key(public_file.read())

            # Read the content of the file to be encrypted
            with open(input_file_path, "rb") as input_file:
                file_data = input_file.read()

            # Encrypt the file content
            encrypted_data = public_key.encrypt(
                file_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=SHA256()),
                    algorithm=SHA256(),
                    label=None
                )
            )

            # Save the encrypted data to the output file
            with open(output_file_path, "wb") as output_file:
                output_file.write(encrypted_data)
            print(f"File encrypted successfully and saved to {output_file_path}")

        except Exception as e:
            print(f"Error encrypting file: {e}")
