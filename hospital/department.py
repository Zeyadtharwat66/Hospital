from files import files
from hospital import hospital
class department(hospital):
    def __init__(self,name='',manger=''):
        self.name = name
        self.manger = manger 

class department():
    def __init__(self,name='',manger=''):
        self.name = name
        self.manger = manger

    def __add_patient_to_dep(self,patient):
        f=files(r"C:\D\Amit\Duo\hospital\patient's_department.txt")
        f.write_to_file(content={f'{department.name}':{"name":f'{patient.name}',"age":f'{patient.age}',"phone_number":f"{patient.phone_number}","arrival_time":f"{patient.arrival_time}","disease":f'{patient.disease}'}},file_name="patient's_department.txt")
    
    def __add_staff_to_dep(self,staff):
        f=files(r"C:\D\Amit\Duo\hospital\staff's_department.txt")
        f.write_to_file(content={f'{department.name}':{"name":f'{staff.name}',"password":f'{staff.password}',"role":f'{staff.role}',"phone_number":f'{staff.phone_number}'}},file_name="staff's_department.txt")

    def get_departments(self):
        f=files(r"C:\D\Amit\Duo\hospital\departments.txt")
        return f.file_to_nested_dictionary()
    
    def get_patient_in_dep():
        f=files(r"C:\D\Amit\Duo\hospital\patient's_department.txt")
        return f.file_to_nested_dictionary()
        
    
    def get_staff_in_dep(self):
        f=files(r"C:\D\Amit\Duo\hospital\staff's_department.txt")
        return f.file_to_nested_dictionary()
        
