import customtkinter as ctk
from tkinter import filedialog, messagebox
from Code import usr_authen, create_folder, key_generate, encrypt, decrypt
from tkinter import PhotoImage
from PIL import Image, ImageTk
import hashlib
import json
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("MILITARY SECRET MESSAGE")
        self.root.geometry("900x800")
        self.page_history = []  # History to keep track of the pages
        ctk.set_appearance_mode("dark")  # Dark mode for modern feel
        ctk.set_default_color_theme("green") 
        self.username = None
        self.email = None

        self.set_background()
        self.create_main_menu()

    def set_background(self):
        self.root.configure(bg="#2F4F4F")
        frame_color = "#4F6D4F"
        self.root.configure(bg=frame_color)

    def create_main_menu(self):
        self.add_logo()
        ctk.CTkLabel(self.root, text="MILITARY SECRET MESSAGE", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=20)

        ctk.CTkButton(self.root, text="Create Account", width=300, height=60, font=("Berlin Sans FB Demi", 18), command=self.create_account, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Login", width=300, height=60, font=("Berlin Sans FB Demi", 18), command=self.login, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Forgot Password", width=300, height=60, font=("Berlin Sans FB Demi", 18), command=self.forgot_password, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)

        ctk.CTkButton(self.root, text="Exit", width=300, height=60, font=("Berlin Sans FB Demi", 18), command=self.root.quit, fg_color="#ff0000", hover_color="#556B2F").pack(pady=20)

    def add_logo(self):
        try:
            # Load the image using PIL
            img = Image.open("MSS.png")
            img = img.resize((250, 200))  # Resize to the desired dimensions

            # Convert the image to a format compatible with customtkinter
            self.logo = ImageTk.PhotoImage(img)

            # Create a label and set the image
            logo_label = ctk.CTkLabel(self.root, image=self.logo)
            logo_label.pack(pady=30)
        except Exception as e:
            print(f"Error loading logo: {e}")

    def create_account(self):
        self.clear_screen()
        self.page_history.append(self.create_main_menu) 

        ctk.CTkLabel(self.root, text="Create Account", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        # Create large input fields
        username_entry = ctk.CTkEntry(self.root, font=("Arial", 18),placeholder_text="  Username", width=300, height=50)
        username_entry.pack(pady=15)

        email_entry = ctk.CTkEntry(self.root, font=("Arial", 18), placeholder_text="  Email", width=300, height=50)
        email_entry.pack(pady=15)

        password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*",placeholder_text="  Password", width=300, height=50)
        password_entry.pack(pady=15)

        confirm_password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*",placeholder_text="  Confirm Password", width=300, height=50)
        confirm_password_entry.pack(pady=15)

        def create_account_action():
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match!")
                return

            authen = usr_authen.Usr_Create(username, password, email)
            if authen.usr_pass() == False:
                messagebox.showerror("Error", "Username already exists!")
            else:
                CreateFd = create_folder.Create_folder(username)
                CreateFd.create_folder()

                # Save email to usr_email.json
                if not os.path.exists("./Files/usr_email.json"):
                    with open("./Files/usr_email.json", "w") as f:
                        json.dump({}, f)

                KeyGenerate = key_generate.RSAkey(username)
                KeyGenerate.generate_key()
                KeyGenerate.save_key()

                messagebox.showinfo("Success", "Account created successfully!")
                self.clear_screen()
                self.create_main_menu()  # After account creation, go back to main menu

        ctk.CTkButton(self.root, text="Create Account", font=("Berlin Sans FB Demi", 18), command=create_account_action, fg_color="#4F6D4F", hover_color="#556B2F", width=150, height=50).pack(pady=20)

        self.create_back_button()


    def login(self):
        self.clear_screen()
        self.page_history.append(self.create_main_menu)

        ctk.CTkLabel(self.root, text="Login", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        username_entry = ctk.CTkEntry(self.root, placeholder_text="Username", font=("Arial", 18), width=300, height=50)
        username_entry.pack(pady=15)

        password_entry = ctk.CTkEntry(self.root, placeholder_text="Password", font=("Arial", 18), show="*", width=300, height=50)
        password_entry.pack(pady=15)

        # Initialize attempts counter and i_label if not already done
        if not hasattr(self, 'login_attempts'):
            self.login_attempts = 3

        if not hasattr(self, 'i_label'):
            self.i_label = ctk.CTkLabel(self.root, text=f"", font=("Arial", 18), text_color="white")
            self.i_label.pack(pady=10)

        def login_action():
            username = username_entry.get()
            password = password_entry.get()
            login = usr_authen.Usr_Create(username, password, email=None)

            if login.usr_login():
    
                messagebox.showinfo("Success", "Login successful!")
                self.username = username
                self.show_operations_menu()
            else:
                self.login_attempts -= 1
                self.i_label.configure(text=f"{self.login_attempts} attempts left!")
                if self.login_attempts == 0:
                    messagebox.showerror("Error", "No attempts left! Access denied.")
                    self.i_label.configure(text="Access denied!")
                    self.go_back()

        ctk.CTkButton(self.root, text="Login", font=("Berlin Sans FB Demi", 18), command=login_action, width=150, height=50).pack(pady=20)

        self.create_back_button()

    def show_operations_menu(self):
        self.clear_screen()
        self.page_history.append(self.show_operations_menu)

        ctk.CTkLabel(self.root, text=f"Welcome, {self.username}", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        ctk.CTkButton(self.root, text="Encrypt", width=300, height=60, font=("Berlin Sans FB Demi", 18), command=self.show_encryption_page, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Decrypt", width=300, height=60, font=("Berlin Sans FB Demi", 18), command=self.show_decryption_page, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Secret Message", width=300, height=60, font=("Berlin Sans FB Demi", 18), fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        self.create_back_button()

    def show_encryption_page(self):
        self.clear_screen()
        self.page_history.append(self.show_operations_menu)

        ctk.CTkLabel(self.root, text="Encrypt Message", font=("Arial", 30), text_color="white").pack(pady=30)

        # Add text input for message to be encrypted
        message_label = ctk.CTkLabel(self.root, text="Enter message to encrypt:", font=("Arial", 18), text_color="white")
        message_label.pack()
        message_entry = ctk.CTkEntry(self.root, font=("Arial", 18), width=300)
        message_entry.pack(pady=10)

        def encrypt_action():
            message = message_entry.get()
            try:
                # Create an instance of the Encryption class
                encryption_instance = encrypt.Encryption(self.username)
                encrypted_message = encryption_instance.encrypt_message(message)
                if encrypted_message:
                    self.encrypt_content_box(encrypted_message)
                else:
                    messagebox.showerror("Error", "Encryption failed!")
            except Exception as e:
                messagebox.showerror("Error", f"Error encrypting message: {e}")


        # Button for message encryption
        ctk.CTkButton(self.root, text="Encrypt", font=("Arial", 18), command=encrypt_action, fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=40).pack(pady=20)

        # Add file selection and encryption button
        def encrypt_file_action():
            file_path = filedialog.askopenfilename(title="Select File to Encrypt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            print(f"Selected file path: {file_path}")  # Debugging line
            if file_path:
                try:
                    # Initialize the Encryption class with the provided username
                    encryption = encrypt.Encryption(self.username)

                    # Read the file content
                    with open(file_path, 'r') as file:
                        file_content = file.read()

                    # Encrypt the file content
                    encrypted_content = encryption.encrypt_message(file_content)
                    if encrypted_content is None:
                        raise ValueError("Encryption failed.")
                    self.encrypt_content_box(encrypted_content)
                except Exception as e:
                    messagebox.showerror("Error", f"Error encrypting file: {e}")


        # Button for file encryption
        ctk.CTkButton(self.root, text="Encrypt File", font=("Arial", 18), command=encrypt_file_action, fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=40).pack(pady=20)

        # Add back button to return to previous page
        self.operation_back_button()


    def show_decryption_page(self):
        self.clear_screen()
        self.page_history.append(self.show_operations_menu)

        ctk.CTkLabel(self.root, text="Decrypt Message", font=("Arial", 30), text_color="white").pack(pady=30)

        # Add text input for message to be decrypted
        message_label = ctk.CTkLabel(self.root, text="Enter message to decrypt:", font=("Arial", 18), text_color="white")
        message_label.pack()
        message_entry = ctk.CTkEntry(self.root, font=("Arial", 18), width=300)
        message_entry.pack(pady=10)

        def decrypt_action():
            message = message_entry.get()
            try:
                # Create an instance of the Decryption class
                decryption_instance = decrypt.Decryption(self.username)
                decrypted_message = decryption_instance.decrypt_message(message)
                if decrypted_message:
                    print(f"Decrypted message: {decrypted_message}")  # Debugging line
                    self.decrypt_content_box(decrypted_message)  # Display decrypted message
                else:
                    messagebox.showerror("Error", "Decryption failed!")
            except Exception as e:
                messagebox.showerror("Error", f"Error decrypting message: {e}")


        # Button for message decryption
        ctk.CTkButton(self.root, text="Decrypt", font=("Arial", 18), command=decrypt_action, fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=40).pack(pady=20)

        # Add file selection and decryption button
        def decrypt_file_action():
            file_path = filedialog.askopenfilename(title="Select File to Decrypt", filetypes=[("Encrypted Files", "*.enc"), ("All Files", "*.*")])
            if file_path:
                try:
                    print(f"Selected file path: {file_path}")  # Debugging line
                    # Initialize the Decryption class with the provided username
                    decryption = decrypt.Decryption(self.username)

                    # Read the encrypted file content
                    with open(file_path, 'r') as file:
                        file_content = file.read()

                    # Decrypt the file content
                    decrypted_content = decryption.decrypt_message(file_content)
                    if decrypted_content is None:
                        raise ValueError("Decryption failed.")
                    self.decrypt_content_box(decrypted_content)  # Display decrypted content
                except Exception as e:
                    messagebox.showerror("Error", f"Error decrypting file: {e}")

        # Button for file decryption
        ctk.CTkButton(self.root, text="Decrypt File", font=("Arial", 18), command=decrypt_file_action, fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=40).pack(pady=20)

        # Add back button to return to previous page
        self.operation_back_button()

    def forgot_password(self):
        self.clear_screen()
        self.page_history.append(self.create_main_menu)

        ctk.CTkLabel(self.root, text="Forgot Password", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        #Ask for username and email
        username_entry = ctk.CTkEntry(self.root, font=("Arial", 18), placeholder_text="Username", width=300, height=50)
        username_entry.pack(pady=15)

        email_entry = ctk.CTkEntry(self.root, font=("Arial", 18), placeholder_text="Enter your registered email", width=300, height=50)
        email_entry.pack(pady=20)

        #Verify the username and email
        def verify_user_action():
            username = username_entry.get()
            email = email_entry.get()

            #Check if email exists in usr_email.json
            try:
                with open("./Files/usr_email.json", "r") as email_file:
                    email_data = json.load(email_file)

                with open("./Files/usr_pass.json", "r") as pass_file:
                    pass_data = json.load(pass_file)

                #Verify if the email and username match
                if email_data.get(username) == email:
                    self.show_recovery_password_page(username, pass_data)
                else:
                    messagebox.showerror("Error", "Username or email not registered!")
            except Exception as e:
                messagebox.showerror("Error", f"Error processing request: {e}")

        ctk.CTkButton(self.root, text="Verify", font=("Berlin Sans FB Demi", 18), command=verify_user_action, fg_color="#4F6D4F", hover_color="#556B2F", width=150, height=50).pack(pady=20)

        self.create_back_button()

    def show_recovery_password_page(self, username, pass_data):
        self.clear_screen()

        ctk.CTkLabel(self.root, text="Reset Password", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        #Allow the user to input a new password
        new_password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*", placeholder_text="Enter new password", width=300, height=50)
        new_password_entry.pack(pady=15)

        confirm_password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*", placeholder_text="Confirm new password", width=300, height=50)
        confirm_password_entry.pack(pady=15)

        #Save the new password and overwrite the old one
        def save_new_password():
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()

            if not new_password or not confirm_password:
                messagebox.showerror("Error", "Password fields cannot be empty!")
                return

            if new_password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match! Please try again.")
                new_password_entry.delete(0, "end")
                confirm_password_entry.delete(0, "end")
                return

            #Hash the new password
            hashed_password = hashlib.sha256(new_password.encode("utf-8")).hexdigest()

            #Update the password in the JSON file
            try:
                if username in pass_data:
                    pass_data[username] = hashed_password

                    #Save the updated passwords
                    with open("./Files/usr_pass.json", "w") as pass_file:
                        json.dump(pass_data, pass_file, indent=4)

                    messagebox.showinfo("Success", "Password has been updated successfully!")
                    self.clear_screen()
                    self.create_main_menu()
                else:
                    messagebox.showerror("Error", "User not found in the system!")
            except Exception as e:
                messagebox.showerror("Error", f"Error updating password: {e}")

        ctk.CTkButton(self.root, text="Save New Password", font=("Berlin Sans FB Demi", 18), command=save_new_password, fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=50).pack(pady=20)

        self.create_back_button()

    def operation_back_button(self):
        ctk.CTkButton(self.root, text="Back", font=("Berlin Sans FB Demi", 18), command=self.operation_go_back, fg_color="#ff0000", hover_color="#556B2F").pack(pady=20)

    def operation_go_back(self):
            self.clear_screen()             
            self.show_operations_menu()

    def create_back_button(self):
        ctk.CTkButton(self.root, text="Back", font=("Berlin Sans FB Demi", 18), command=self.go_back, fg_color="#ff0000", hover_color="#556B2F").pack(pady=20)

    def go_back(self):
        self.clear_screen()  
        self.create_main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        # Reset attributes
        if hasattr(self, 'encrypted_frame'):
            self.encrypted_frame = None
        if hasattr(self, 'decrypted_frame'):
            self.decrypted_frame = None


    def encrypt_content_box(self, encrypt_content):
        # Reset encrypted_frame if it exists to avoid referencing a destroyed widget
        if hasattr(self, 'encrypted_frame') and self.encrypted_frame:
            self.encrypted_frame.destroy()
        
        # Create a new encrypted frame
        self.encrypted_frame = ctk.CTkFrame(self.root, width=400, height=150, fg_color="#333333", corner_radius=10)
        self.encrypted_frame.pack(pady=10)

        # Add a label for the encrypted message
        ctk.CTkLabel(self.encrypted_frame, text="Encrypted Contents", font=("Arial", 14), text_color="white").pack(pady=5)

        # Add a textbox for the encrypted message (copyable)
        encrypted_box = ctk.CTkTextbox(self.encrypted_frame, width=480, height=200, font=("Arial", 12), text_color="white", fg_color="#222222", wrap="word")
        encrypted_box.pack(pady=5, padx=10)
        encrypted_box.insert("1.0", encrypt_content)  # Insert the encrypted message
        encrypted_box.configure(state="disabled")  # Make it read-only

        def save_as_action():
            save_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc"), ("All Files", "*.*")], title="Save Decrypted File")
            if save_path:  # Only save if the user selected a path
                messagebox.showinfo("File Saved", f"File saved as: {save_path}")

        ctk.CTkButton(self.encrypted_frame, text="Save As", width=300, height=40, font=("Berlin Sans FB Demi", 14), fg_color="#4F6D4F", hover_color="#556B2F", command=save_as_action).pack(pady=10)

    def decrypt_content_box(self, decrypt_content):
        # Reset decrypted_frame if it exists to avoid referencing a destroyed widget
        if hasattr(self, 'decrypted_frame') and self.decrypted_frame:
            self.decrypted_frame.destroy()

        # Create a new decrypted frame
        self.decrypted_frame = ctk.CTkFrame(self.root, width=400, height=150, fg_color="#333333", corner_radius=10)
        self.decrypted_frame.pack(pady=10)

        # Add a label for the decrypted message
        ctk.CTkLabel(self.decrypted_frame, text="Decrypted Contents", font=("Arial", 14), text_color="white").pack(pady=5)

        # Add a textbox for the decrypted message (copyable)
        decrypted_box = ctk.CTkTextbox(self.decrypted_frame, width=480, height=200, font=("Arial", 12), text_color="white", fg_color="#222222", wrap="word")
        decrypted_box.pack(pady=5, padx=10)
        decrypted_box.insert("1.0", decrypt_content)  # Insert the decrypted message
        decrypted_box.configure(state="disabled")  # Make it read-only


        def save_as_action():
            save_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc"), ("All Files", "*.*")], title="Save Decrypted File")
            if save_path:  # Only save if the user selected a path
                messagebox.showinfo("File Saved", f"File saved as: {save_path}")

        ctk.CTkButton(self.decrypted_frame, text="Save As", width=300, height=40, font=("Berlin Sans FB Demi", 14), fg_color="#4F6D4F", hover_color="#556B2F", command=save_as_action).pack(pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
