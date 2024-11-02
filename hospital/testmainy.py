from person import person
from staff import staff
from hospital import hospital
from department import department
from patient import patient
if __name__ == '__main__':#3shan hwa intrepreter 
    choose=input("choose 1 if u r a staff member and 0 if u r patient ")
    if choose=="1":
        y=input("choose 1 if u want to sign up and 0 for login ")
        if y=="1":
            name=input("enter ur name : ")
            age=input("enter ur age : ")
            phone_number=input('enter phone number')
            role=input('enter role')
            password=input('enter password')
            email=input('enter email')
            confirm_password=input('enter confirm password')
            s=staff(name, age, phone_number, role, password, email)#s is object 
            s.signup(confirm_password)
        elif y=="0":
            email=input('enter email')
            password=input("enter your password")
            staff().login(email, password)
            