import hashlib
import json

class Usr_Create:
    def __init__(self,usr_name,usr_passwd,email):
        self.usr_name=usr_name
        self.__usr_passwd=usr_passwd
        self.email=email
        
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
        
        try:
            usr_email_dict={self.usr_name:self.email}
            try:
                with open("./Files/usr_email.json","r") as file: 
                    content=file.read().strip()
                    if not content:
                        with open("./Files/usr_email.json","w") as f:
                            json.dump(usr_email_dict,f,indent=4)
                    if content:
                        new_data=json.loads(content)
                        if self.usr_name in new_data:
                            print(f"The username:{self.usr_name} is already existed")
                            return False
                        else:
                            new_data[self.usr_name]=self.email
                            with open("./Files/usr_email.json","w") as f:
                                json.dump(new_data,f,indent=4)
            except Exception as e:
                print(e)
                 
        except Exception as e:
            print(e)
            
    def usr_login(self):
        try:
            if len(self.__usr_passwd) == 64:
                try:
                    with open("./Files/usr_pass.json","r") as file:
                        user=json.load(file)
                        if self.usr_name in user and self.__usr_passwd==user[self.usr_name]:
                            return(True)
                except Exception as e:
                    print(e)  
            else:
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
            
class pass_recover:
    def __init__(self,username,new_passwd,email):
        self.username=username
        self.__new_passwd=new_passwd
        self.email=email
    def check_for_pass(self):
        try:
            with open("./Files/usr_pass.json","r") as file:
                data=json.load(file)
                if(self.username in data):
                    with open("./Files/usr_email.json","r") as f:
                        us_em=json.load(f)
                        if(self.email == us_em[self.username]):
                            passwd = hashlib.sha256()
                            passwd.update(self.__new_passwd.encode("utf-8"))
                            hashed_pass=passwd.hexdigest()
                            data[self.username]=hashed_pass
                            with open("./Files/usr_pass.json","w") as f:
                                json.dump(data,f,indent=4)
                            return True
                        else:
                            return False 
                else:
                    return False

        except Exception as e:
            print(e)
        


