import tkinter as tk
import customtkinter as ctk
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Code import encrypt, decrypt, usr_authen, key_generate, create_folder  # Import your operations

# Global label variables
error_label = None
success_label = None

# Function to create an account
def create_account():
    global error_label, success_label  # Reference the global variables

    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Ensure error_label is created
    if not error_label:  # If the error label is not initialized
        error_label = ctk.CTkLabel(root, text="", text_color="red")
    
    # Clear any previous error messages
    error_label.configure(text="")
    success_label.configure(text="") if success_label else None

    # If passwords do not match
    if password != confirm_password:
        error_label.configure(text="Passwords do not match. Please try again.")
        error_label.pack(pady=10)
        return

    # Simulate account creation (you can add actual validation and creation logic here)
    if username and password:  # Add your validation logic here
        # Create folder and generate keys
        CreateFd = create_folder.Create_folder(username)
        CreateFd.create_folder()

        KeyGenerate = key_generate.RSAkey(username)
        KeyGenerate.generate_key()
        KeyGenerate.save_key()

        # Create a success message
        if not success_label:
            success_label = ctk.CTkLabel(root, text="Account created successfully!", text_color="green")
        success_label.pack(pady=10)
        
        # Optionally, clear the input fields
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)
    else:
        error_label.configure(text="Account creation failed. Try again.")
        error_label.pack(pady=10)

# Function to show the main menu
def main_menu():
    clear_frame()
    
    title_label = ctk.CTkLabel(root, text="MNF Encryption and Decryption", font=("Arial", 20, "bold"), text_color="#2d3e50")
    title_label.pack(pady=20)

    # Create Account Button
    sign_up_button = ctk.CTkButton(root, text="Sign Up", command=show_sign_up, width=200, height=40)
    sign_up_button.pack(pady=10)

    # Login Button
    login_button = ctk.CTkButton(root, text="Login", command=show_login, width=200, height=40)
    login_button.pack(pady=10)

    # Forget Password Button
    forget_password_button = ctk.CTkButton(root, text="Forgot Password", command=show_forget_password, width=200, height=40)
    forget_password_button.pack(pady=10)

    # Exit Button
    exit_button = ctk.CTkButton(root, text="Exit", command=root.quit, fg_color="red", hover_color="#cc0000", width=200, height=40)
    exit_button.pack(pady=10)

# Function to clear the current frame
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# Show Sign Up screen
def show_sign_up():
    clear_frame()

    # Sign Up Title
    sign_up_title_label = ctk.CTkLabel(root, text="Create Account", font=("Arial", 20, "bold"), text_color="#2d3e50")
    sign_up_title_label.pack(pady=20)

    # Username and Password Fields
    username_label = ctk.CTkLabel(root, text="Username:")
    username_label.pack(pady=5)
    global username_entry
    username_entry = ctk.CTkEntry(root, width=200)
    username_entry.pack(pady=5)

    password_label = ctk.CTkLabel(root, text="Password:")
    password_label.pack(pady=5)
    global password_entry
    password_entry = ctk.CTkEntry(root, width=200, show="*")
    password_entry.pack(pady=5)

    confirm_password_label = ctk.CTkLabel(root, text="Confirm Password:")
    confirm_password_label.pack(pady=5)
    global confirm_password_entry
    confirm_password_entry = ctk.CTkEntry(root, width=200, show="*")
    confirm_password_entry.pack(pady=5)

    # Create Account Button
    create_account_button = ctk.CTkButton(root, text="Create Account", command=create_account, width=200, height=40)
    create_account_button.pack(pady=10)

    # Back Button
    back_button = ctk.CTkButton(root, text="Back", command=main_menu, width=200, height=40)
    back_button.pack(pady=10)

# Show Login screen
def show_login():
    clear_frame()

    # Login Title
    login_title_label = ctk.CTkLabel(root, text="Login", font=("Arial", 20, "bold"), text_color="#2d3e50")
    login_title_label.pack(pady=20)

    # Username and Password Fields
    login_username_label = ctk.CTkLabel(root, text="Username:")
    login_username_label.pack(pady=5)
    global login_username_entry
    login_username_entry = ctk.CTkEntry(root, width=200)
    login_username_entry.pack(pady=5)

    login_password_label = ctk.CTkLabel(root, text="Password:")
    login_password_label.pack(pady=5)
    global login_password_entry
    login_password_entry = ctk.CTkEntry(root, width=200, show="*")
    login_password_entry.pack(pady=5)

    # Login Button
    login_button = ctk.CTkButton(root, text="Login", command=login, width=200, height=40)
    login_button.pack(pady=10)

    # Back Button
    back_button = ctk.CTkButton(root, text="Back", command=main_menu, width=200, height=40)
    back_button.pack(pady=10)

# Function to handle login
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    # Authenticate user with your usr_authen
    login_auth = usr_authen.Usr_Create(username, password)

    if login_auth.usr_login():
        success_label = ctk.CTkLabel(root, text="Login successful!", text_color="green")
        success_label.pack(pady=10)
    else:
        error_label = ctk.CTkLabel(root, text="Login failed. Try again.", text_color="red")
        error_label.pack(pady=10)

# Function to handle forget password
def show_forget_password():
    clear_frame()

    # Forget Password Title
    forget_password_title_label = ctk.CTkLabel(root, text="Forget Password", font=("Arial", 20, "bold"), text_color="#2d3e50")
    forget_password_title_label.pack(pady=20)

    # Username Field
    forget_password_username_label = ctk.CTkLabel(root, text="Enter your username:")
    forget_password_username_label.pack(pady=5)
    global forget_password_username_entry
    forget_password_username_entry = ctk.CTkEntry(root, width=200)
    forget_password_username_entry.pack(pady=5)

    # Reset Password Button
    reset_password_button = ctk.CTkButton(root, text="Reset Password", command=forget_password, width=200, height=40)
    reset_password_button.pack(pady=10)

    # Back Button
    back_button = ctk.CTkButton(root, text="Back", command=main_menu, width=200, height=40)
    back_button.pack(pady=10)

# Simulate forget password functionality
def forget_password():
    print("Forget password functionality coming soon!")
    main_menu()  # Return to main menu after forget password

# Run the application
root = ctk.CTk()
root.title("MNF Encryption and Decryption")
root.geometry("500x600")  # Set window size (adjust as needed)

# Set theme for customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

main_menu()  # Show the main menu initially

root.mainloop()
