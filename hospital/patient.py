from person import person

class patient(person):

    def __init__(self,name,age,phone_number,arrival_time,email,disease=''):
        super().__init__(name,age,phone_number)
        self.arrival_time=arrival_time
        self.disease=disease
    @classmethod
    def set_medical_disease(cls,email,disease):
        pass
    @classmethod
    def medical_record(cls,email):
        pass
    @classmethod
    def personal_record(cls,email):# get patient info from file patient
        pass
