from person import person
from staff import staff
from hospital import hospital
from department import department
from patient import patient
import time 
if __name__ == '__main__':
    choose=input("choose 1 if u r a staff member and 2 if u r patient ")
    if choose=="1":
        y=input("choose 1 if u want to sign up and 2 for login ")
        if y=="1":
            name=input("enter ur name : ")
            age=input("enter ur age : ")
            phone_number=input('enter phone number: ')
            role=input('enter role: ')
            password=input('enter password: ')
            email=input('enter email: ')
            confirm_password=input('enter confirm password ')
            print('c  '+confirm_password +'  '+password)
            s=staff(name, age, phone_number, role, email, password)
            s.signup(confirm_password)
        elif y=="2":
            email=input('enter email: ')
            password=input("enter your password: ")
            staff().login(email, password)
        else:
            print("invalid input")
            #continue
        y=input("choose if u want to add patient press 1\n  press 2 for get your info view info\n press 3 to get patient info")
        if y == "1":
            name=input('enter name: ')
            age=input('enter age: ')
            phone_number=input('enter phone_number: ')
            arrival_time=time.time()
            disease=input('enter disease: ')
            p=patient(name,age,phone_number,arrival_time,disease)
            staff().add_my_patien(p,email)
            
        elif y=="2":
            staff().view_info(email)
        elif y=='3':
                pass
        else:
            print('invalid input')
            #continue
    elif choose=="2":
        emailp=input("Enter email address")
        
        y= input('if you wont set medical disease press 1 \nif you wont show medical record press 2 \nif you wont show personal record press 3 \n')
        if y == '1':
            disease=input("enter disease: ")
            patient().set_medical_disease(emailp,disease)
        elif y=='2':
            patient().medical_record(emailp)
        elif y=='3':
            patient().personal_record(emailp)
        else:
            print('invalid input')
    else:
        print('invalid input')