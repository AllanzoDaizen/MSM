# MILITARY SECRET MESSAGE

Military Secret Message is a Python application that allows users to create secure accounts, encrypt and decrypt messages or files, and communicate securely with others in localhost. This tool leverages RSA encryption to ensure data security. This tool supports both `CLI` and `GUI`.

## Table of Contents
- [MILITARY SECRET MESSAGE](#military-secret-message)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [How to Use](#how-to-use)
    - [Run the Application](#run-the-application)
    - [Options](#options)
  - [File Structure](#file-structure)
  - [Security](#security)
  - [Contributing](#contributing)
  - [License](#license)
  - [Overview](#overview)

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
 
## Overview
