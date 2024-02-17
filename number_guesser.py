import random

 #random.randrange does not include the value 10

#random.randint is used to include the end number

top_of_range =input("Type a Number :")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    
    if top_of_range<=0:
        print("Please type a number larger than 0 next Time")
        quit()
else:
    print('Please type a number next time.')
    quit()


random_number=random.randrange(0,top_of_range)
guess=0

while True:
    guess+=1
    user_guess =input("Make a Guess :")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
         print('Please type a number next time.')
         continue
     
    if user_guess == random_number:
        print("you got it")
        break
    elif user_guess>random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
        
print("You got it in ",guess, " guesses")
        