#define the function needed  add sub div multiplication
# print option to the User 
#Ask for Values 
# call for the function 

def add(a,b):
    ans =a+b
    print(str(a)+"+"+str(b)+"="+str(ans)+"\n")
    
def sub(a,b):
    ans =a-b
    print(str(a)+"-"+str(b)+"="+str(ans)+"\n")
    
def mul(a,b):
    ans =a*b
    print(str(a)+"*"+str(b)+"="+str(ans)+"\n")

def div(a,b):
    ans =a/b
    print(str(a)+"/"+str(b)+"="+str(ans)+"\n")
  
print("Basic Simple Calculator ")
print("-----------------------")
while True:  
    print("A.Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Division")
    print("E.Exit")
    choice =input("Enter Your Choice :")
    if choice =='a'or choice=='A':
        print("Addition")
        a=int(input("Enter the First Number "))
        b=int(input("Enter the second Number "))
        add(a,b)
    elif choice =='b' or choice == 'B':
        print("Subtraction")
        a=int(input("Enter the First Number "))
        b=int(input("Enter the second Number "))
        sub(a,b)
    elif choice =='c' or choice == 'C':
        print("Multiplication")
        a=int(input("Enter the First Number "))
        b=int(input("Enter the second Number "))
        mul(a,b)
    elif choice =='d'or choice== 'D':
        print("Division")
        a=int(input("Enter the First Number "))
        b=int(input("Enter the second Number "))
        div(a,b)
    elif choice =='e'or choice == 'E':
        print("Program Ended ")
        quit()
        