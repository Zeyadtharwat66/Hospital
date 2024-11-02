from person import person
class staff(person):
    def __init__(self,name="",age="",phone_number="",role="",email="",password=""):
        super().__init__(name,age,phone_number,email,password)
        self.role=role
    @classmethod
    def view_info(cls,email):#get imfo from staff file
        pass
    def get_my_patients(self):#get from patient file
        pass
    @classmethod
    def add_my_patien(cls,pat):#update patient file
        pass
    @classmethod
    def login(cls,email,password):
        pass    
    def signup(self,confirm_password):
        if not self.password == confirm_password:
            raise 'warning'
        #
        #انو اليوسر مينفعش يكون مستخدم
        #
        dic = {self.name:{ "email":self.email, "password":self.password,"age":self.age,"role":self.role}}
        print(dic[self.name])


