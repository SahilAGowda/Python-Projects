#ask the user weather they want to generate the password or not
#if yes ask for password length
#generate the password
#Display the password

import string 
import random

character =list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_password():
    password_length=int(input("Enter the Length of the Password ? "))
    random.shuffle(character)
    password=[]
    for x in range(password_length):
        password.append(random.choice(character))
        
    random.shuffle(password)
    
    password ="".join(password)
    print(password)



option =input("Do you Want to Generate the Password (Yes/No) :")

if option.lower() =="yes":
    generate_password()
elif option.lower() == "no":
    print("Program Ended !")
    quit()
else:
    print("Invalid Input please Enter a Valid Input")