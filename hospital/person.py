from files import files
class person():
    ID=0
    def __init__(self,name='',age='',phone_number="0",email="",password=""):
        self.age=age
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.password=password
        person.ID+=1
        print(person.ID)

    def view_info(self,role,email):# get info from file user
        if role=="patient":
            f=files(r"C:\D\Amit\Duo\hospital\patient.txt")
            x=f.file_to_nested_dictionary()
            return x[email]
        elif role=="staff":
            f=files(r"C:\D\Amit\Duo\hospital\staff.txt")
            x=f.file_to_nested_dictionary()
            return x[email]
        else:
            return "Unfound Person"
