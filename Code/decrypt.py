import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from base64 import b64decode

class Decryption:
    def __init__(self, username):
        self.username = username
        self.private_key_path = f"./Files/{self.username}/{self.username}private.pem"
        
        # Ensure the directory exists for private key
        if not os.path.exists(os.path.dirname(self.private_key_path)):
            raise FileNotFoundError(f"Private key directory for user '{self.username}' does not exist.")
        
    def decrypt_message(self, encrypted_message_b64):
        try:
            # Decode the Base64 encoded encrypted message
            encrypted_message = b64decode(encrypted_message_b64)

            # Load the private key from the file
            with open(self.private_key_path, "rb") as private_file:
                private_key = serialization.load_pem_private_key(private_file.read(), password=None)

            # Decrypt the message
            decrypted_message = private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=SHA256()),  # Mask Generation Function
                    algorithm=SHA256(),  # Hashing algorithm
                    label=None
                )
            )

            # Decode the decrypted message back to a string
            return decrypted_message.decode()

        except Exception as e:
            print(f"Error decrypting message: {e}")
            return None
    
    def decrypt_file(self, input_file_path, output_file_path):
        try:
            # Load the private key from the file
            with open(self.private_key_path, "rb") as private_file:
                private_key = serialization.load_pem_private_key(private_file.read(), password=None)

            # Read the encrypted content of the file
            with open(input_file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()

            # Decrypt the file content
            decrypted_data = private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=SHA256()),
                    algorithm=SHA256(),
                    label=None
                )
            )

            # Save the decrypted data to the output file
            with open(output_file_path, "wb") as output_file:
                output_file.write(decrypted_data)
            print(f"File decrypted successfully and saved to {output_file_path}")

        except Exception as e:
            print(f"Error decrypting file: {e}")
            return None
