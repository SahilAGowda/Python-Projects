import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    
    return roll

while True:
    players=input("Enter the Number of the Players(2-4) : ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print('Invalid,Try Again')
        
max_score =50
player_score =[0 for _ in range(players)]

while max(player_score)<max_score:
    for player_idx in range(players):
        print("\nPlayer Number ",player_idx+1,"turn has Just Started \n")
        print("Your Total Score is :",player_score[player_idx],"\n")
        current_score=0
        while True:
            should_roll=input("Would you like to roll!")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("You Rolled a 1!Turn Done !")
                break
            else:
                current_score+=value
                print(f"You Rolled a {value}!")
            
            print("Your score is :",current_score)
            
            
        player_score[player_idx]+=current_score
        print("Your Total SCore is :",player_score[player_idx])
        
max_score=max(player_score)
winning_idx=player_score.index(max_score)
print("Player Number",winning_idx+1,"is the winner with a score of :",max_score)       
        
        


    
    
    
    
    

