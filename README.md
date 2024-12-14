# MNF Encryption and Decryption

MNF Encryption and Decryption is a Python-based application that allows users to create secure accounts, encrypt and decrypt messages or files, and communicate securely with others. This tool leverages RSA encryption to ensure data security.

## Features

- **Account Management**: Create accounts with unique usernames and passwords.
- **Login System**: Secure authentication for users.
- **Message Encryption and Decryption**:
  - Encrypt plain text messages.
  - Decrypt encrypted messages.
- **File Encryption and Decryption**:
  - Encrypt files for secure storage.
  - Decrypt files to access original content.
- **Password Recovery**: Recover lost passwords using a verified email.
- **Secret Chat**: Exchange secure messages with other registered users.

---

## Prerequisites

- Python 3.x
- Required Libraries:
  - `pycryptodome`
  - `json`
  - `hashlib`

Install the dependencies using:
```bash
pip install pycryptodome
```

---

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
```

2. Navigate to the project directory:
```bash
cd MNF-Encryption-Decryption
```

3. Ensure all dependencies are installed.

---

## How to Use

### Run the Application
```bash
python main.py
```

### Options

1. **Create Account**:
   - Provide a username, email, and password.
   - RSA keys are automatically generated and stored securely.

2. **Login**:
   - Enter your username and password to access the system.
   - After logging in, you can:
     - Encrypt/Decrypt Messages
     - Encrypt/Decrypt Files
     - Chat securely with other users

3. **Password Recovery**:
   - Recover your password by verifying your username and registered email.

4. **Exit**:
   - Exit the application.

---

## File Structure

- `main.py`: Entry point of the application.
- `Code/`
  - `encrypt.py`: Handles message and file encryption.
  - `decrypt.py`: Handles message and file decryption.
  - `usr_authen.py`: User authentication and management.
  - `key_generate.py`: RSA key generation.
  - `create_folder.py`: Creates user-specific folders for key storage.
  - `secret_user.py`: Handles secret chat functionality.

---

## Security

- Uses RSA encryption for secure data handling.
- Passwords are hashed using SHA256 for additional security.
- Encryption keys are generated and stored uniquely for each user.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or suggestions, please contact:
- **Name**: [Your Name]
- **Email**: [Your Email]
