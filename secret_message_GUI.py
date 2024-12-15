import tkinter as tk
from tkinter import messagebox
import threading
import socket
from Code import encrypt, decrypt, usr_authen
import customtkinter as ctk  # Assuming you're using customtkinter for styled widgets

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.page_history = []
        self.login_attempts = 3  # Number of allowed login attempts
        self.i_label = None  # Initialize attempts counter label
        self.username = None
        self.target_name = None
        self.peer_socket = None
        self.is_connected = False

        # Set the appearance mode to dark and default color theme to green
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Set the background of the window
        self.set_background()

        # Start with the login page
        self.setup_login()

    def set_background(self):
        """ Set background color and frame color for the window """
        self.root.configure(bg="#2F4F4F")  # Dark background color
        frame_color = "#4F6D4F"  # Greenish frame color
        self.root.configure(bg=frame_color)

    def setup_login(self):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Login", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        # Username entry field
        username_entry = ctk.CTkEntry(self.root, placeholder_text="Username", font=("Arial", 18), width=300, height=50)
        username_entry.pack(pady=15)

        # Password entry field
        password_entry = ctk.CTkEntry(self.root, placeholder_text="Password", font=("Arial", 18), show="*", width=300, height=50)
        password_entry.pack(pady=15)

        # Initialize the attempts counter label
        if not self.i_label:
            self.i_label = ctk.CTkLabel(self.root, text=f"{self.login_attempts} attempts left", font=("Arial", 18), text_color="white")
            self.i_label.pack(pady=10)

        def login_action():
            username = username_entry.get()
            password = password_entry.get()
            # Assuming 'usr_authen.Usr_Create' is a class used for authentication
            login = usr_authen.Usr_Create(username, password, email=None)

            if login.usr_login():
                messagebox.showinfo("Success", "Login successful!")
                self.username = username
                self.secret_message_page()
            else:
                self.login_attempts -= 1
                self.i_label.configure(text=f"{self.login_attempts} attempts left!")
                if self.login_attempts == 0:
                    messagebox.showerror("Error", "No attempts left! Access denied.")
                    self.i_label.configure(text="Access denied!")
                    self.go_back()

        # Login button
        ctk.CTkButton(self.root, text="Login", font=("Berlin Sans FB Demi", 18), command=login_action, width=150, height=50).pack(pady=20)

        # Back button if necessary (optional)
        self.create_back_button()

    def create_back_button(self):
        # Define the back button for navigating back to the login screen (if needed)
        def back_action():
            self.setup_login()
        
        ctk.CTkButton(self.root, text="Back", font=("Arial", 14), command=back_action, width=100, height=40).pack(pady=10)

    def clear_screen(self):
        """ Clears the current screen before showing a new page """
        for widget in self.root.winfo_children():
            widget.destroy()

    def message_callback(self, message):
        """ Update GUI from the main thread using after() to avoid threading issues """
        self.root.after(0, lambda: self.secret_box.insert("end", f"{message}\n"))

    def secret_message_page(self):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Secret Message", font=("Berlin Sans FB Demi", 30), text_color="white").pack(pady=30)

        target_entry = ctk.CTkEntry(self.root, font=("Arial", 18), placeholder_text="Target's username", width=300, height=50)
        target_entry.pack(pady=15)

        ctk.CTkLabel(self.root, text="Enter your secret message", font=("Arial", 14), text_color="white").pack(pady=10)
        message_entry = ctk.CTkEntry(self.root, font=("Arial", 18), placeholder_text="Type your message...", width=300, height=50)
        message_entry.pack(pady=10)

        self.secret_box = ctk.CTkTextbox(self.root, width=480, height=200, font=("Arial", 12), text_color="white", fg_color="#222222", wrap="word")
        self.secret_box.pack(pady=10, padx=10)

        def connect_to_peer():
            if self.is_connected:
                self.message_callback("Already connected to a peer.")
                return

            target_username = target_entry.get().strip()
            if not target_username:
                self.message_callback("Error: Target username cannot be empty.")
                return

            self.message_callback(f"Connecting to {target_username}...")

            def setup_peer():
                try:
                    peer_socket = peer(self.username, target_username, self.message_callback)  # Initiate peer connection
                    if peer_socket:
                        self.peer_socket = peer_socket  # Store peer socket in the GUI instance
                        self.is_connected = True  # Mark as connected
                        self.message_callback(f"Connection established with {target_username}.")

                        # Start listening for incoming messages
                        threading.Thread(target=self.listen_for_messages, args=(self.peer_socket,)).start()
                    else:
                        self.message_callback(f"Failed to connect to {target_username}.")
                except Exception as e:
                    self.message_callback(f"Error connecting to peer: {e}")

            threading.Thread(target=setup_peer).start()

        def send_message():
            message = message_entry.get().strip()
            if not message:
                self.message_callback("Error: Message cannot be empty.")
                return

            if self.peer_socket:
                threading.Thread(target=self.send_mes, args=(self.peer_socket, self.username, message)).start()
                self.message_callback(f"Me: {message}")
            else:
                self.message_callback("Error: No active connection.")

        ctk.CTkButton(self.root, text="Connect", font=("Berlin Sans FB Demi", 18), command=connect_to_peer,
                      fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=50).pack(pady=10)

        ctk.CTkButton(self.root, text="Send Message", font=("Berlin Sans FB Demi", 18), command=send_message,
                      fg_color="#4F6D4F", hover_color="#556B2F", width=200, height=50).pack(pady=10)

        self.create_back_button()

    def listen_for_messages(self, peer_socket):
        """ Start listening for messages from the peer """
        threading.Thread(target=listen, args=(peer_socket, self.username, self.message_callback)).start()

    def send_mes(self, peer_socket, username, message):
        """ Send encrypted message """
        try:
            message_encrypt = encrypt.Encryption(username)
            encrypted_message = message_encrypt.encrypt_message(message).encode('utf-8')
            peer_socket.send(encrypted_message)
        except Exception as e:
            self.message_callback(f"Error sending message: {e}")

def peer(username, target_username, message_callback):
    """ Simulate peer connection for demonstration purposes """
    try:
        peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer_ip = "localhost"
        peer_port = 2000

        try:
            peer_socket.connect((peer_ip, peer_port))
            message_callback(f"Connected to {target_username}")
            return peer_socket
        except socket.error as e:
            message_callback(f"Connection error: {e}")
            return None
    except Exception as e:
        message_callback(f"Error setting up peer connection: {e}")
        return None

def main():
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
