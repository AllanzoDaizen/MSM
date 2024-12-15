# Secure Ops

Secure Ops is a Python application that allows users to create secure accounts, encrypt and decrypt messages or files, and communicate securely with others in localhost. 
This tool leverages RSA encryption to ensure data security. This tool supports both `CLI` and `GUI`.

## Table of Contents
- [Secure Ops](#secure-ops)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [How to Use](#how-to-use)
    - [Run the Application](#run-the-application)
    - [Options](#options)
  - [File Structure](#file-structure)
  - [Security](#security)
  - [Contributing](#contributing)
  - [Project Overview](#project-overview)
    - [CLI APLLICATION](#cli-apllication)
    - [GUI APPLICATION](#gui-application)
  - [Conclusion](#conclusion)

## Features

- **Account Management**: Create accounts with unique usernames and passwords.
- **Login System**: Secure authentication for users.
- **Message Encryption and Decryption**:
  - Encrypt plain text messages.
  - Decrypt encrypted messages.
- **File Encryption and Decryption using path of file**:
  - Encrypt files for secure storage.
  - Decrypt files to access original content.
- **Password Recovery**: Recover lost passwords using a verified email.
- **Secret Chat**: Exchange secure messages with other registered users.

---

## Installation
- **Clone the repository**:
``` bash
    git clone https://github.com/AllanzoDaizen/MSM.git
```
---

- **Required Libraries:**
  - `pycryptodome`
  - `json`
  - `hashlib`
  - `customtkinter` 
  - `PIL`
  
- **Install the dependencies using:**
```bash
pip install pycryptodome
```
```bash
pip install hashlib
```
```bash
pip install tkinter
```
```bash
pip install customtkinter
```
```bash
pip install PIL
```

1. Navigate to the project directory:
```bash
cd MSM
```

---

## How to Use

### Run the Application
- **For CLI**:
```bash
python main.py
```
- **For GUI**:
```bash
python GUI.py
```

### Options

1. **Create Account**:
   - Provide a username, email, and password.
   - RSA keys are automatically generated and stored securely in a unique folder.

2. **Login**:
   - Enter your username and password to access the system.
   - User have 3 attempts to Login.
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
- `GUI.py`: GUI of the application.
- `README.md`: Handles the application details.
- `Code/`
  - `encrypt.py`: Handles message and file encryption.
  - `decrypt.py`: Handles message and file decryption.
  - `usr_authen.py`: User authentication and management.
  - `key_generate.py`: RSA key generation.
  - `create_folder.py`: Creates user-specific folders for key storage.
  - `secret_user.py`: Handles secret chat functionality.
- `Assets/`
  - `MSS.png`: logo of application.
- `File/`
  - `User-directory`: a unique directory for each user.
---

## Security

- Uses RSA encryption for secure data handling.
- Passwords are hashed using SHA256 for additional security.
- Encryption keys are generated and stored uniquely for each user.


---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.


---
 
## Project Overview
### CLI APLLICATION
- Menu
  - ![Screenshot 2024-12-15 220156](https://github.com/user-attachments/assets/0d074a74-1a81-4026-8e3c-216764cf6b06)
- Create Account
  - ![image](https://github.com/user-attachments/assets/4b544bfd-8e7e-491d-9db0-9fde588a7340)
- Login ( After login successful, the operation menu will be appeared )
  - ![image](https://github.com/user-attachments/assets/cf2e23d3-0ead-4383-9268-232ee6f9dd88)
- Operation ( Message )
  - ![image](https://github.com/user-attachments/assets/e1d81dc7-a25a-46fc-b720-0165d81189da)
- Operation ( Files )
  - ![image](https://github.com/user-attachments/assets/abe5e4ed-40a3-4c74-ba1a-8d0d98ddf74a)
- Operation ( Secret Chat )
It is a testing, this function supports only the in local machine. You can run 2 terminals to test it. 
- ![image](https://github.com/user-attachments/assets/4376e9a1-8765-430d-a817-7227fb498b9b)
- To exit this operation type "exit"
- Forget password
- ![image](https://github.com/user-attachments/assets/883eaedd-23c3-4da9-8444-972e7ba77576)

### GUI APPLICATION

- In this project, by having some problems with GUI platfom to handle the P2P connection, We haven't done the Secret Message part in our GUI application.
- Menu
- ![image](https://github.com/user-attachments/assets/bd20a218-9b62-425a-983b-31e770f756cd)
- Create Account
- ![image](https://github.com/user-attachments/assets/7ff5d780-c5a1-4943-8b64-4bf9c6fd375e)
- Login
- ![image](https://github.com/user-attachments/assets/46b5188b-bec6-4f24-a0ac-353a0a011f51)
- After login successfully, the operation menu will be appeared.
- ![image](https://github.com/user-attachments/assets/ad40c92c-3b46-4227-9345-300d7b5fc17a)
- Both encrypt and decrypt have the same templat.
- ![image](https://github.com/user-attachments/assets/d17245e3-741b-46c3-8d4f-fe9210aedcc3)
- Forgot Password
- ![image](https://github.com/user-attachments/assets/b8967257-62c3-48a9-99d1-648394878ff2)
- After verify both username and email successful,
- ![image](https://github.com/user-attachments/assets/a081bca4-20e9-4593-9692-6a7d7a60d42a)

## Conclusion
SecureOps is a python project that created to allow users to encrypt or decrypt their data securely.
Finally, Thank you for reading this `README.md` and supporting our project.







  



