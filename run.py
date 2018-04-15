import json

def quiz(riddle):
    """Asks the riddle question and takes the users answer to match the official answer"""
    answer = input(riddle["question"] + " ")

    if right_answer(answer, riddle): #will take the answer of each riddle
            print("Correct! Well done.\nYour score is",score)
        
    else: 
        print("Your answer is wrong")

def right_answer(answer,riddle):
    return answer == riddle["answer"]

def main():
    with open("riddles.json") as riddles_file:
        riddles = json.load(riddles_file)

    for riddle in riddles: #loops through the quiz questions
        print(quiz(riddle))
