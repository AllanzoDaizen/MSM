import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from Code import usr_authen, encrypt, decrypt, create_folder, key_generate

# Set up the green theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class App():
    def __init__(self):
        self.title("Encryption and Decryption App")
        self.geometry("600x400")

        # Add menu bar
        self.menu = ctk.CTkMenu(self)
        self.config(menu=self.menu)

        self.menu.add_command(label="Create Account", command=self.create_account)
        self.menu.add_command(label="Login", command=self.login)
        self.menu.add_command(label="Forget Password", command=self.forget_password)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.quit)

    def create_account(self):
        self.clear_frame()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.username_label = ctk.CTkLabel(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ctk.CTkEntry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = ctk.CTkLabel(self.frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = ctk.CTkEntry(self.frame)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = ctk.CTkLabel(self.frame, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = ctk.CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.confirm_password_label = ctk.CTkLabel(self.frame, text="Confirm Password:")
        self.confirm_password_label.grid(row=3, column=0, padx=10, pady=10)
        self.confirm_password_entry = ctk.CTkEntry(self.frame, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

        self.create_button = ctk.CTkButton(self.frame, text="Create Account", command=self.process_create_account)
        self.create_button.grid(row=4, column=0, columnspan=2, pady=10)

    def process_create_account(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        authen = usr_authen.Usr_Create(username, password, email)
        if authen.usr_pass() == False:
            messagebox.showerror("Error", "Username already exists")
            return

        # Create user folder and generate keys
        create_folder.Create_folder(username).create_folder()
        key_gen = key_generate.RSAkey(username)
        key_gen.generate_key()

        messagebox.showinfo("Success", "Account created successfully!")
        self.clear_frame()

    def login(self):
        self.clear_frame()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.username_label = ctk.CTkLabel(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ctk.CTkEntry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = ctk.CTkLabel(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ctk.CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.process_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def process_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        login = usr_authen.Usr_Create(username, password, email=None)
        if login.usr_login():
            messagebox.showinfo("Success", "Login successful!")
            self.main_operation(username)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def main_operation(self, username):
        self.clear_frame()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.encrypt_button = ctk.CTkButton(self.frame, text="Message Encryption/Decryption", command=lambda: self.message_encrypt_decrypt(username))
        self.encrypt_button.grid(row=0, column=0, padx=10, pady=10)

        self.file_encrypt_button = ctk.CTkButton(self.frame, text="File Encryption/Decryption", command=lambda: self.file_encrypt_decrypt(username))
        self.file_encrypt_button.grid(row=1, column=0, padx=10, pady=10)

        self.logout_button = ctk.CTkButton(self.frame, text="Logout", command=self.clear_frame)
        self.logout_button.grid(row=2, column=0, padx=10, pady=10)

    def message_encrypt_decrypt(self, username):
        self.clear_frame()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.message_label = ctk.CTkLabel(self.frame, text="Enter Message:")
        self.message_label.grid(row=0, column=0, padx=10, pady=10)
        self.message_entry = ctk.CTkEntry(self.frame)
        self.message_entry.grid(row=0, column=1, padx=10, pady=10)

        self.encrypt_button = ctk.CTkButton(self.frame, text="Encrypt", command=lambda: self.encrypt_message(username))
        self.encrypt_button.grid(row=1, column=0, padx=10, pady=10)

        self.decrypt_button = ctk.CTkButton(self.frame, text="Decrypt", command=lambda: self.decrypt_message(username))
        self.decrypt_button.grid(row=1, column=1, padx=10, pady=10)

    def encrypt_message(self, username):
        message = self.message_entry.get()
        encryptor = encrypt.Encryption(username)
        encryptor.encrypt_message(message)

    def decrypt_message(self, username):
        message = self.message_entry.get()
        decryptor = decrypt.Decryption(username)
        decryptor.decrypt_message(message)

    def file_encrypt_decrypt(self, username):
        self.clear_frame()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.file_label = ctk.CTkLabel(self.frame, text="Select File Path:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_entry = ctk.CTkEntry(self.frame)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)

        self.encrypt_button = ctk.CTkButton(self.frame, text="Encrypt", command=lambda: self.encrypt_file(username))
        self.encrypt_button.grid(row=1, column=0, padx=10, pady=10)

        self.decrypt_button = ctk.CTkButton(self.frame, text="Decrypt", command=lambda: self.decrypt_file(username))
        self.decrypt_button.grid(row=1, column=1, padx=10, pady=10)

    def encrypt_file(self, username):
        file_path = self.file_entry.get()
        output_path = file_path + ".enc"
        encryptor = encrypt.Encryption(username)
        encryptor.encrypt_file(file_path, output_path)

    def decrypt_file(self, username):
        file_path = self.file_entry.get()
        output_path = file_path + ".dec"
        decryptor = decrypt.Decryption(username)
        decryptor.decrypt_file(file_path, output_path)

    def forget_password(self):
        self.clear_frame()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.username_label = ctk.CTkLabel(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ctk.CTkEntry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = ctk.CTkLabel(self.frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = ctk.CTkEntry(self.frame)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.new_password_label = ctk.CTkLabel(self.frame, text="New Password:")
        self.new_password_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_password_entry = ctk.CTkEntry(self.frame, show="*")
        self.new_password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.confirm_new_password_label = ctk.CTkLabel(self.frame, text="Confirm New Password:")
        self.confirm_new_password_label.grid(row=3, column=0, padx=10, pady=10)
        self.confirm_new_password_entry = ctk.CTkEntry(self.frame, show="*")
        self.confirm_new_password_entry.grid(row=3, column=1, padx=10, pady=10)

        self.recover_button = ctk.CTkButton(self.frame, text="Recover Password", command=self.process_password_recovery)
        self.recover_button.grid(row=4, column=0, columnspan=2, pady=10)

    def process_password_recovery(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_new_password_entry.get()

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        recovery = usr_authen.pass_recover()
        if recovery.check_email(username, email):
            if recovery.change_pass(username, new_password):
                messagebox.showinfo("Success", "Password changed successfully!")
                self.clear_frame()
            else:
                messagebox.showerror("Error", "Error changing password")
        else:
            messagebox.showerror("Error", "Invalid username or email")

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
