from person import person
class staff(person):
    def __init__(self,name,age,phone_number,role,email="",password=""):
        super().__init__(name,age,phone_number,email,password)
        self.role=role
    def view_info(self):#get imfo from staff file
        pass
    def get_my_patients(self):#get from patient file
        pass
    def add_my_patients(self):#update patient file
        pass
    def login(self):
        pass