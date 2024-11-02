class person():
    ID=0
    def __init__(self,name='',age='',phone_number=0,email="",password=""):
        self.age=age
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.password=password
        person.ID+=1
        print(person.ID)
        
        
    def view_info(self):# getv info from file user
        pass
