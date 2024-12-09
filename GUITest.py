import customtkinter as ctk
from tkinter import filedialog, messagebox
from Code import usr_authen, create_folder, key_generate, encrypt, decrypt
from tkinter import PhotoImage
from PIL import Image, ImageTk

class MNFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MNF Encryption & Decryption")
        self.root.geometry("900x700")
        self.username = None

        # Stack to track page history
        self.page_history = []

        # Set the theme
        ctk.set_appearance_mode("dark")  # Dark mode for modern feel
        ctk.set_default_color_theme("green")  # Military green color theme

        # Set the background color to a military mix (olive green, brown)
        self.set_background()

        # Create buttons for the main menu
        self.create_main_menu()

    def set_background(self):
        # Setting a military-style color gradient (green and brown mix)
        self.root.configure(bg="#2F4F4F")  # Main background color

        # For the frame color, use a camo brown tone
        frame_color = "#4F6D4F"
        self.root.configure(bg=frame_color)

    def create_main_menu(self):
        # Add the logo at the start page
        self.add_logo()

        ctk.CTkLabel(self.root, text="MNF Encryption and Decryption Tool", font=("Arial", 30), text_color="white").pack(pady=30)

        # Create larger buttons with a military color theme
        ctk.CTkButton(self.root, text="Create Account", width=300, height=60, font=("Arial", 18), command=self.create_account, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Login", width=300, height=60, font=("Arial", 18), command=self.login, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Exit", width=300, height=60, font=("Arial", 18), command=self.root.quit, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)

    def add_logo(self):
        try:
            # Load the image using PIL
            img = Image.open("Military.png")
            img = img.resize((200, 200))  # Resize to the desired dimensions
            
            # Convert the image to a format compatible with customtkinter
            self.logo = ImageTk.PhotoImage(img)
            
            # Create a label and set the image
            logo_label = ctk.CTkLabel(self.root, image=self.logo)
            logo_label.pack(pady=20)
        except Exception as e:
            print(f"Error loading logo: {e}")

    def create_account(self):
        self.clear_screen()
        self.page_history.append(self.create_main_menu)

        ctk.CTkLabel(self.root, text="Create Account", font=("Arial", 30), text_color="white").pack(pady=30)

        # Create large input fields
        username_label = ctk.CTkLabel(self.root, text="Username:", font=("Arial", 18), text_color="white")
        username_label.pack()
        username_entry = ctk.CTkEntry(self.root, font=("Arial", 18), width=300)
        username_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self.root, text="Password:", font=("Arial", 18), text_color="white")
        password_label.pack()
        password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*", width=300)
        password_entry.pack(pady=10)

        confirm_password_label = ctk.CTkLabel(self.root, text="Confirm Password:", font=("Arial", 18), text_color="white")
        confirm_password_label.pack()
        confirm_password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*", width=300)
        confirm_password_entry.pack(pady=10)

        def create_account_action():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match!")
                return

            authen = usr_authen.Usr_Create(username, password)
            if authen.usr_pass() == False:
                messagebox.showerror("Error", "Username already exists!")
            else:
                CreateFd = create_folder.Create_folder(username)
                CreateFd.create_folder()
                KeyGenerate = key_generate.RSAkey(username)
                KeyGenerate.generate_key()
                KeyGenerate.save_key()
                messagebox.showinfo("Success", "Account created successfully!")
                self.clear_screen()
                self.create_main_menu()

        ctk.CTkButton(self.root, text="Create Account", font=("Arial", 18), command=create_account_action, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=30)
        
        # Add back button to return to previous page
        self.create_back_button()

    def login(self):
        self.clear_screen()
        self.page_history.append(self.create_main_menu)

        ctk.CTkLabel(self.root, text="Login", font=("Arial", 30), text_color="white").pack(pady=30)

        username_label = ctk.CTkLabel(self.root, text="Username:", font=("Arial", 18), text_color="white")
        username_label.pack()
        username_entry = ctk.CTkEntry(self.root, font=("Arial", 18), width=300)
        username_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self.root, text="Password:", font=("Arial", 18), text_color="white")
        password_label.pack()
        password_entry = ctk.CTkEntry(self.root, font=("Arial", 18), show="*", width=300)
        password_entry.pack(pady=10)

        def login_action():
            username = username_entry.get()
            password = password_entry.get()

            login = usr_authen.Usr_Create(username, password)
            if login.usr_login():
                self.username = username
                messagebox.showinfo("Success", "Login successful!")
                self.show_operations_menu()
            else:
                messagebox.showerror("Error", "Login failed!")

        ctk.CTkButton(self.root, text="Login", font=("Arial", 18), command=login_action, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=30)

        # Add back button to return to previous page
        self.create_back_button()

    def show_operations_menu(self):
        self.clear_screen()
        self.page_history.append(self.create_main_menu)
        ctk.CTkLabel(self.root, text=f"Welcome, {self.username}", font=("Arial", 30), text_color="white").pack(pady=30)

        ctk.CTkButton(self.root, text="Message Encryption/Decryption", font=("Arial", 18), width=300, height=60, command=self.message_operations, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="File Encryption/Decryption", font=("Arial", 18), width=300, height=60, command=self.file_operations, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Logout", font=("Arial", 18), width=300, height=60, command=self.logout, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)

        # Add back button to return to previous page
        self.create_back_button()

    def message_operations(self):
        self.clear_screen()
        self.page_history.append(self.show_operations_menu)

        ctk.CTkLabel(self.root, text="Message Operations", font=("Arial", 30), text_color="white").pack(pady=30)

        def encrypt_message():
            message = message_entry.get()
            encryption = encrypt.Encryption(self.username)
            encryption.encrypt_message(message)

        def decrypt_message():
            message = message_entry.get()
            decryption = decrypt.Decryption(self.username)
            decryption.decrypt_message(message)

        ctk.CTkLabel(self.root, text="Enter Message:", font=("Arial", 18), text_color="white").pack(pady=10)
        message_entry = ctk.CTkEntry(self.root, font=("Arial", 18), width=300)
        message_entry.pack(pady=10)

        ctk.CTkButton(self.root, text="Encrypt Message", font=("Arial", 18), command=encrypt_message, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Decrypt Message", font=("Arial", 18), command=decrypt_message, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)

        # Add back button to return to previous page
        self.create_back_button()

    def file_operations(self):
        self.clear_screen()
        self.page_history.append(self.show_operations_menu)

        ctk.CTkLabel(self.root, text="File Operations", font=("Arial", 30), text_color="white").pack(pady=30)

        def encrypt_file():
            file_path = filedialog.askopenfilename()
            encryption = encrypt.Encryption(self.username)
            encryption.encrypt_file(file_path)

        def decrypt_file():
            file_path = filedialog.askopenfilename()
            decryption = decrypt.Decryption(self.username)
            decryption.decrypt_file(file_path)

        ctk.CTkButton(self.root, text="Encrypt File", font=("Arial", 18), command=encrypt_file, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)
        ctk.CTkButton(self.root, text="Decrypt File", font=("Arial", 18), command=decrypt_file, fg_color="#4F6D4F", hover_color="#556B2F").pack(pady=20)

        # Add back button to return to previous page
        self.create_back_button()

    def create_back_button(self):
        ctk.CTkButton(self.root, text="Back", font=("Arial", 18), command=self.go_back, fg_color="#4F6D4F", hover_color="#556B2F").place(x=30, y=30)

    def go_back(self):
        if self.page_history:
            self.clear_screen()
            previous_page = self.page_history.pop()
            previous_page()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def logout(self):
        self.username = None
        self.clear_screen()
        self.create_main_menu()

if __name__ == "__main__":
    root = ctk.CTk()
    app = MNFApp(root)
    root.mainloop()
