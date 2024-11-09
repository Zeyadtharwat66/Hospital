from person import person
from files import files
class patient(person):

    def __init__(self,name="",age="",phone_number="",arrival_time="",email="",disease=''):
        super().__init__(name,age,phone_number)
        self.arrival_time=arrival_time
        self.disease=disease
        self.email=email
        if not(name=="" and age=="" and phone_number==""):
            f=files(r"C:\D\Duo\hospital\patient.txt")
            f.write_to_file(content={f'{self.email}':{"name":f'{self.name}',"age":f'{self.age}',"phone_number":f"{self.phone_number}","arrival_time":f"{self.arrival_time}","disease":f'{self.disease}'}},file_name="patient.txt")
    @classmethod
    def set_medical_disease(cls, email, disease):
        f=files(r"C:\D\Duo\hospital\patient.txt")
        content=f.file_to_nested_dictionary()
        if disease not in content[email]["disease"]:
            if content[email]["disease"]:
                content[email]["disease"] += "," + disease
            else:
                content[email]["disease"] = disease
        else:
            print(f"Disease '{disease}' is already recorded for this patient.")
            return
        f.update_file(content=content, file_name="patient.txt")
        
    @classmethod
    def medical_record(cls,email):
        f=files(r"C:\D\Duo\hospital\patient.txt")
        content=f.file_to_nested_dictionary()
        return content[email]["disease"]
    @classmethod
    def personal_record(cls,email):# get patient info from file patient
        f=files(r'C:\D\Duo\hospital\patient.txt')
        content=f.file_to_nested_dictionary()
        return content[email]
