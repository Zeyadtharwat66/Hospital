from person import person
from files import files
class staff(person):
    def __init__(self,name="",age="",phone_number="",role="",email="",password=""):
        super().__init__(name,age,phone_number,email,password)
        self.role=role
    @classmethod
    def view_info(cls,email):#get imfo from staff file
        f=files(r'C:\Users\Lenovo\Desktop\shared_github\staff.txt')
        content=f.file_to_nested_dictionary()
        for i in content.values():
            if i['email']==email:
                return i
    @classmethod
    def login(cls,email,password):
        f=files(r'C:\Users\Lenovo\Desktop\shared_github\staff.txt')
        content=f.file_to_nested_dictionary()
        flag = False
        for i in content.values():
            if i['email'] == email and i['password'] == password:
                flag=True
        if flag:
            return 'login successful'
        else:
            raise 'worning'
    def signup(self,confirm_password):
        f=files(r'C:\Users\Lenovo\Desktop\shared_github\staff.txt')
        if not self.password == confirm_password:
            raise 'warning'
        content=f.file_to_nested_dictionary()
        if self.name in content.keys():
            raise 'warning'
        f.write_to_file('staff.txt',content={self.name:{'age':self.age, 'phone_number':self.phone_number,'role':self.role, 'email':self.email}})


