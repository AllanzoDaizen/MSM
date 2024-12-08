import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Code import key_generate, create_folder, usr_authen, encrypt, decrypt

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("MNF Encryption and Decryption")
        self.root.geometry("800x400")

        self.username = None
        self.password = None

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        # Centering the title label
        title_label = tk.Label(self.root, text="MNF Encryption and Decryption", font=("Helvetica", 20))
        title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")

        # Creating buttons with centering and left-right padding
        create_account_button = tk.Button(self.root, text="CREATE ACCOUNT", command=self.create_account, font=("Helvetica", 13))
        create_account_button.grid(row=1, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

        login_button = tk.Button(self.root, text="LOG IN", command=self.login, font=("Helvetica", 13))
        login_button.grid(row=2, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

        forget_pass_button = tk.Button(self.root, text="FORGOT PASSWORD", command=self.forget_pass, font=("Helvetica", 13))
        forget_pass_button.grid(row=3, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

        exit_button = tk.Button(self.root, text="EXIT", command=self.root.quit, font=("Helvetica", 13))
        exit_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Configure grid columns for centering
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def create_account(self):
        self.clear_window()

        username_label = tk.Label(self.root, text="Enter username")
        username_label.grid(row=0, column=0, pady=5, sticky="w", padx=20)

        username_entry = tk.Entry(self.root)
        username_entry.grid(row=0, column=1, pady=5, padx=20)

        password_label = tk.Label(self.root, text="Enter password")
        password_label.grid(row=1, column=0, pady=5, sticky="w", padx=20)

        password_entry = tk.Entry(self.root, show="*")
        password_entry.grid(row=1, column=1, pady=5, padx=20)

        confirm_password_label = tk.Label(self.root, text="Confirm password")
        confirm_password_label.grid(row=2, column=0, pady=5, sticky="w", padx=20)

        confirm_password_entry = tk.Entry(self.root, show="*")
        confirm_password_entry.grid(row=2, column=1, pady=5, padx=20)

        def on_submit():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            # Call the relevant method for account creation
            authen = usr_authen.Usr_Create(username, password)
            if authen.usr_pass() == False:
                messagebox.showerror("Error", "Username already exists!")
            else:
                # Account created successfully
                create_folder.Create_folder(username).create_folder()
                key_gen = key_generate.RSAkey(username)
                key_gen.generate_key()
                messagebox.showinfo("Success", "Account created successfully!")
                self.main_menu()

        submit_button = tk.Button(self.root, text="Submit", command=on_submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

        back_button = tk.Button(self.root, text="Back", command=self.main_menu)
        back_button.grid(row=4, column=0, columnspan=2, padx=20)

        # Configure grid columns for centering the input elements
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def login(self):
        self.clear_window()

        username_label = tk.Label(self.root, text="Enter username")
        username_label.grid(row=0, column=0, pady=5, sticky="w", padx=20)

        username_entry = tk.Entry(self.root)
        username_entry.grid(row=0, column=1, pady=5, padx=20)

        password_label = tk.Label(self.root, text="Enter password")
        password_label.grid(row=1, column=0, pady=5, sticky="w", padx=20)

        password_entry = tk.Entry(self.root, show="*")
        password_entry.grid(row=1, column=1, pady=5, padx=20)

        def on_login():
            username = username_entry.get()
            password = password_entry.get()

            authen = usr_authen.Usr_Create(username, password)
            if authen.usr_login():
                messagebox.showinfo("Success", "Login successful!")
                self.username = username
                self.show_operations_menu()
            else:
                messagebox.showerror("Error", "Login failed!")

        login_button = tk.Button(self.root, text="Login", command=on_login)
        login_button.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

        back_button = tk.Button(self.root, text="Back", command=self.main_menu)
        back_button.grid(row=3, column=0, columnspan=2, padx=20)

        # Configure grid columns for centering the login fields
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def show_operations_menu(self):
        self.clear_window()

        title_label = tk.Label(self.root, text=f"Welcome {self.username}", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")

        message_encryption_button = tk.Button(self.root, text="Message Encryption", command=self.message_encryption)
        message_encryption_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        file_encryption_button = tk.Button(self.root, text="File Encryption", command=self.file_encryption)
        file_encryption_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        exit_button = tk.Button(self.root, text="Logout", command=self.main_menu)
        exit_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # Label for showing results of encryption/decryption
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12), fg="green")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Configure grid columns for centering the operation buttons
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def message_encryption(self):
        self.clear_window()

        message_label = tk.Label(self.root, text="Enter message to encrypt")
        message_label.grid(row=0, column=0, pady=5, sticky="w", padx=20)

        message_entry = tk.Entry(self.root)
        message_entry.grid(row=0, column=1, pady=5, padx=20)

        def on_encrypt():
            message = message_entry.get()
            encrypt_obj = encrypt.Encryption(self.username)
            encrypted_message = encrypt_obj.encrypt_message(message)

            # Display encrypted message in the result label
            self.result_label.config(text=f"Encrypted Message: {encrypted_message}")

        encrypt_button = tk.Button(self.root, text="Encrypt", command=on_encrypt)
        encrypt_button.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        back_button = tk.Button(self.root, text="Back", command=self.show_operations_menu)
        back_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20)

        # Configure grid columns for centering
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def file_encryption(self):
        self.clear_window()

        file_label = tk.Label(self.root, text="Choose a file to encrypt")
        file_label.grid(row=0, column=0, pady=5, sticky="w", padx=20)

        def on_file_select():
            file_path = filedialog.askopenfilename()
            if file_path:
                save_path = filedialog.asksaveasfilename(defaultextension=".enc")
                encrypt_obj = encrypt.Encryption(self.username)
                encrypt_obj.encrypt_file(file_path, save_path)

                # Display success message after encryption
                self.result_label.config(text=f"File encrypted and saved to: {save_path}")

        select_file_button = tk.Button(self.root, text="Select File", command=on_file_select)
        select_file_button.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

        back_button = tk.Button(self.root, text="Back", command=self.show_operations_menu)
        back_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20)

        # Configure grid columns for centering the file operation
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def forget_pass(self):
        pass

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
