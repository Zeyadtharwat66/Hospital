from person import person

class patient(person):

    def __init__(self,name,age,phone_number,arrival_time,leaving_time,email="",password="",disease=''):
        super().__init__(name,age,phone_number,email,password)
        self.arrival_time=arrival_time
        self.leaving_time=leaving_time
        self.disease=disease
    def set_medical_disease(self,disease):
        pass
    def medical_record(self):
        pass
    def personal_record(self):# get patient info from file patient
        pass
