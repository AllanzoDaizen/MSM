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
                with open("C:\\Users\\USER\\OneDrive - Cambodia Academy of Digital Technology\\Desktop\\MSM\\Files\\usr_pass.json","r") as file: 
                    content=file.read().strip()
                    if not content:
                        with open("C:\\Users\\USER\\OneDrive - Cambodia Academy of Digital Technology\\Desktop\\MSM\\Files\\usr_pass.json","w") as f:
                            json.dump(usr_pass_dict,f,indent=4)
                    if content:
                        new_data=json.loads(content)
                        if self.usr_name in new_data:
                            print(f"The username:{self.usr_name} is already existed")
                        else:
                            new_data[self.usr_name]=hashed_pass
                            with open("C:\\Users\\USER\\OneDrive - Cambodia Academy of Digital Technology\\Desktop\\MSM\\Files\\usr_pass.json","w") as f:
                                json.dump(new_data,f,indent=4)
            except Exception as e:
                print(e)
                 
        except Exception as e:
            print(e)

#Testing       
usr1=Usr_Create("Thanan","123456")
usr1.usr_pass()
usr3=Usr_Create("kinin","345345")
usr3.usr_pass()
usr4=Usr_Create("sreynich","samnang")
usr4.usr_pass()
