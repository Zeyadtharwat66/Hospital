from hospital import hospital
from person import person
from staff import staff
from patient import patient
import time 
if __name__ == '__main__':
    h=hospital(location="Alexandria, Egypt",name="Elite Hospital")
    print(f"{h.name}")
    print(f"{h.location}")
    choose=input("choose 1 if You are a staff member and 2 if you are patient : ")
    if choose=="1":
        y=input("choose 1 if you want to sign up and 2 for login : ")
        if y=="1":
            name=input("enter your name : ")
            age=input("enter your age : ")
            phone_number=input('enter phone number : ')
            role=input('enter role : ')
            password=input('enter password : ')
            email=input('enter email : ')
            confirm_password=input('enter confirm password : ')
            print('c  '+confirm_password +'  '+password)
            s=staff(name, age, phone_number, role, email, password)
            s.signup(confirm_password)
        elif y=="2":
            email=input('enter email : ')
            password=input("enter your password : ")
            staff().login(email, password)
        else:
            print("invalid input")
            #continue   
        y=input("choose if you want to add patient press 1\n  press 2 for get your info view info\n press 3 to get patient info")
        if y == "1":
            name=input('enter name : ')
            age=input('enter age : ')
            phone_number=input('enter phone number : ')
            arrival_time=time.time()
            disease=input('enter disease : ')
            emailz=input('enter email : ')
            p=patient(name,age,phone_number,arrival_time,emailz,disease)           
        elif y=="2":
            print(staff().view_info(email))
        elif y=='3':
            emailz=input('enter patient\'s email : ')
            print(patient().personal_record(emailz))
        else:
            print('invalid input')
            #continue
    elif choose=="2":
        emailp=input("Enter email address : ")
        y= input('if you want set medical disease press 1 \nif you want show medical record press 2 \nif you want show personal record press 3 \n')
        if y == '1':
            disease=input("enter disease : ")
            print(patient().set_medical_disease(emailp,disease))
        elif y=='2':
            print(patient().medical_record(emailp))
        elif y=='3':
            print(patient().personal_record(emailp))
        else:
            print('invalid input')
    else:
        print('invalid input')