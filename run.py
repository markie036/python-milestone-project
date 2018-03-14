import json

def quiz(riddle):
    """Asks the riddle question and takes the users answer to match the official answer"""
    answer = input(riddle["question"] + " ")

    return answer == riddle["answer"] #will take the answer of each riddle

with open("riddles.json") as riddles_file:
    riddles = json.load(riddles_file)


for riddle in riddles: #loops through the quiz questions
    print(quiz(riddle))



