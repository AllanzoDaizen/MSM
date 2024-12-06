import os 
class Create_folder:
    def __init__(self, username):
         self.username = username
    def create_folder(self):
            folder_name = f"./Files/{self.username}"
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            else:
                print(f"User '{folder_name}' already exists.")
