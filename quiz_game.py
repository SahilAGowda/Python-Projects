print("Welcome to my computer quiz")

playing=input("Do You want to play? ")

if playing.lower()!="yes":
    quit()

print("Okay! Lets Play :)")
score=0

answer =input("What does CPU Stand for ?\n")

if answer.lower()== "central processing unit":
    print ("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")

answer =input("What does GPU Stand for ?\n")

if answer.lower() == "graphics processing unit":
    print ("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")


answer =input("What does RAM Stand for ?\n")

if answer.lower() == "random access memory":
    print ("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")

answer =input("What does PSU Stand for ?\n")

if answer.lower() =="power supply unit":
    print ("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")
    
print("You get "+str(score) +" question correct !")
print("You get "+str((score/4)*100)  +" %.")