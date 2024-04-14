#Collect Email from the User 
# Split the email using the @ first part as the user name 
# second part is gonna be domain by splitting it

def main():
    print("Welcome to the Email Slicer :")
    print("---------------------------");
    
    email_input=input("Enter your Email Address")
    (username,domain)=email_input.split("@")  # it is used to store the first part of the variable with the username and after @ it will be in domain part
    (domain,extension)=domain.split(".")
    
    print("Username : ",username)
    print("Domain : ",domain)
    print("Extension : ",extension)
    

while True:
    main()