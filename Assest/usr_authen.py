import hashlib
import json

class Usr_Create:
    def __init__(self,usr_name,usr_passwd):
        self.usr_name=usr_name
        self.__usr_passwd=usr_passwd
        
    def usr_pass(self):
        try:
            data = hashlib.sha256()
            data.update(self.__usr_passwd.encode("utf-8"))
            hashed_pass=data.hexdigest()
            usr_pass_dict={self.usr_name:hashed_pass}
            try:
                with open("./Files/usr_pass.json","r") as file: 
                    content=file.read().strip()
                    if not content:
                        with open("./Files/usr_pass.json","w") as f:
                            json.dump(usr_pass_dict,f,indent=4)
                    if content:
                        new_data=json.loads(content)
                        if self.usr_name in new_data:
                            print(f"The username:{self.usr_name} is already existed")
                            return False
                        else:
                            new_data[self.usr_name]=hashed_pass
                            with open("./Files/usr_pass.json","w") as f:
                                json.dump(new_data,f,indent=4)
            except Exception as e:
                print(e)
                 
        except Exception as e:
            print(e)
            
    def usr_login(self):
        try:
            data=hashlib.sha256()
            data.update(self.__usr_passwd.encode("utf-8"))
            log_passwd=data.hexdigest()
            try:
                with open("./Files/usr_pass.json","r") as file:
                    user=json.load(file)
                    if self.usr_name in user and log_passwd==user[self.usr_name]:
                        return(True)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


