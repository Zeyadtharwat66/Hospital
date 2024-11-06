from person import person
from files import files
class patient(person):

    def __init__(self,name,age,phone_number,arrival_time,email,disease=''):
        super().__init__(name,age,phone_number)
        self.arrival_time=arrival_time
        self.disease=disease
    @classmethod
    def set_medical_disease(cls, email, disease):
        f=files(r"C:\D\Amit\Duo\hospital\patient.txt")
        content=f.file_to_nested_dictionary()
        content[email]["disease"]+=","+disease
        f.update_file(content=content,file_name="patient.txt")
        
    @classmethod
    def medical_record(cls,email):
        f=files(r"C:\D\Amit\Duo\hospital\patient.txt")
        content=f.file_to_nested_dictionary()
        return content[email]["disease"]
    @classmethod
    def personal_record(cls,email):# get patient info from file patient
        f=files(r"C:\D\Amit\Duo\hospital\patient.txt")
        content=f.file_to_nested_dictionary()
        return content[email]
