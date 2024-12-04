import os 
class Create_folder:
    def __init__(self, username):
         self.username = username
    def create_folder(self):
            folder_name = f"./Files/{self.username}"
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(f"Folder '{folder_name}' created successfully!")
            else:
                print(f"Folder '{folder_name}' already exists.")
