#import random
# define a function to a roll the dice
#create a dictionary that will have the drawing of the dice 
#create a directory that will have the value of the dices
import random


def roll_dice():
    dice_drawing={
        1:{
            "__________",
           "|          |",
           "|     1    |",
           "|__________|",            
        },
        2:{
            "__________",
           "|          |",
           "|     2    |",
           "|__________|",           
        },
        3:{
            "__________",
           "|          |",
           "|     3    |",
           "|__________|",            
        },
        4:{
            "__________",
           "|          |",
           "|     4    |",
           "|__________|",            
        },
        5:{
            "__________",
           "|          |",
           "|     5    |",
           "|__________|",           
        },
        6:{
            "__________",
           "|          |",
           "|     6yes    |",
           "|__________|", 
                 
        },
        
        
    }
    roll=input("Do you want to Roll the dice (Yes/No):")
    while roll.lower()=="yes":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        
        print("dice rolled:{} and {}".format(dice1,dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        roll=input("Do you want to Roll Again(Yes/No):")
        
roll_dice()