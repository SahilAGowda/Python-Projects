# have a dictionary that stores question and answer 
# have a variable that track the score of the player
# Loop through the dictionary using key value pair
# Display each question to the user and allow to answer and show them the points 

quiz={
    "question1":{
        "question":"What is the Capital of France ?",
        "answer":"Paris"
    },
    "question2":{
        "question":"What is the Capital of Germany ?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"What is the Capital of Italy ?",
        "answer":"Rome"
    },
    "question4":{
        "question":"What is the Capital of Spain ?",
        "answer":"Madrid"
    },
    "question5":{
        "question":"What is the Capital of Portugal ?",
        "answer":"Lisbon"
    },
    "question6":{
        "question":"What is the Capital of Switzerland ?",
        "answer":"Bern"
    },
    "question7":{
        "question":"What is the Capital of Austria?",
        "answer":"Vienna"
    },
    
}
score=0
for key,value in quiz.items():
    print(value['question'])
    answer =input("Answer?")
    if answer.lower()==value['answer'].lower():
        print("Correct")
        score=score+1
        print("Your Score is : "+str(score))
        print("")
    else:
        print("InCorrect !")
        print("The Answer is:"+value['answer'])
        print("Your Score is : "+str(score))
        print("")
        
print("You Got "+str(score)+" out of 7 Question Correctly")
print("Your Percentage is :"+str(int(score/7*100))+"%")