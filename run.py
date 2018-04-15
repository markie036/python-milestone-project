import json

score = 0

def quiz(riddle):
    counter = 0
    
    while counter < 3:
        """Asks the riddle question and takes the users answer to match the official answer"""
        answer = input(riddle["question"] + " ")
    
        if right_answer(answer, riddle): #will take the answer of each riddle
            global score
            score +=1
            print("Correct! Well done.\nYour score is",score)
            break
        
        else: 
            wrong_answer(answer, riddle)
            print("Your score is", score)
            counter +=1

def right_answer(answer,riddle):
    return answer == riddle["answer"]
    
def wrong_answer(answer, riddle): 
    if answer != riddle["answer"]:
        print("Sorry", answer, "is wrong.")


with open("riddles.json") as riddles_file:
    riddles = json.load(riddles_file)

for riddle in riddles: #loops through the quiz questions
    print(quiz(riddle))
