from files import files
from patient import patient
from department import department
class hospital:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        
    def add_dep(self,dep):
        f=files(r"C:\D\Amit\Duo\hospital\departments.txt")
        f.write_to_file(content={f'{dep.name}':{"manger":f'{dep.manger}'}},file_name="departments.txt")
    
    def add_patient(self,patient:patient):#to file
        f=files(r"C:\D\Amit\Duo\hospital\patient.txt")
        f.write_to_file(content={f'{patient.email}':{"name":f'{patient.name}',"age":f'{patient.age}',"phone_number":f"{patient.phone_number}","arrival_time":f"{patient.arrival_time}","disease":f'{patient.disease}'}},file_name="patient.txt")
    
    def add_staff(self,staff):#to file
        f=files(r"C:\D\Amit\Duo\hospital\staff.txt")
        f.write_to_file(content={f'{staff.email}':{"name":f'{staff.name}',"password":f'{staff.password}',"role":f'{staff.role}',"phone_number":f'{staff.phone_number}'}},file_name="staff.txt")
    
    def get_all_staffs(self):
        f=files(r"C:\D\Amit\Duo\hospital\staff.txt")
        return f.file_to_nested_dictionary()
    
    def get_all_patients(self):
        f=files(r"C:\D\Amit\Duo\hospital\patient.txt")
        return f.file_to_nested_dictionary()
    
s=hospital(location="Egypt",name="ELITE")
s.add_dep(department(name="Zeyad",manger="DR.Khaled"))
s.add_patient(patient(name="khaled",age="24",phone_number="011486566665",arrival_time="12:50",email="ziad@gmail.com",disease='backache'))
print(s.get_all_patients())