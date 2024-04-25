import random

exit = True
user_points = 0
computer_points = 0
while True:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock,paper,scissors or exit")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended ")
        print("You won a total score of "+str(user_points)+" and the computer total score is "+str(computer_points))
        exit = False

    if user_input == "rock" :
        if computer_input == "paper":
            print("Your input is rock and computer input is paper")
            print("You lose")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock and computer input is scissors")
            print("You win")
            user_points += 1
        elif computer_input == "rock":
            print("Your input is rock and computer input is rock")
            print("It is a tie")

    elif user_input == "paper":
        if computer_input == "scissors":
            print("Your input is paper and computer input is scissors")
            print("You lose")
            computer_points += 1
        elif computer_input == "rock":
            print("Your input is paper and computer input is rock")
            print("You win")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper and computer input is paper")
            print("It is a tie")

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors and computer input is rock")
            print("You lose")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors and computer input is paper")
            print("You win")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors and computer input is scissors")
            print("It is a tie")


    elif user_input!= "rock" or user_input!= "paper" or user_input!= "scissors":
        print("InValid Choice ")
        
