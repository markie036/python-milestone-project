import json


score = 0
max_guesses = 3

def quiz(riddle):
    
    counter = 0
    
    while counter < max_guesses:
        "Asks the riddle question and takes the users answer to match the official answer"
        answer = input(riddle["question"] + " ")

        if right_answer(answer, riddle):
            global score
            score += 1
            print("Correct! Well done.\nYour score is",score)
            break
        
        else: 
            counter +=1
            wrong_answer(answer, riddle)
            no_of_guesses(answer, counter)
            print("Your score is", score)

def right_answer(answer, riddle):
    return answer == riddle["answer"]
    
def wrong_answer(answer, riddle): 
    if answer != riddle["answer"]:
        print("Sorry", answer, "is wrong.")
        
def no_of_guesses(answer, counter):
    if answer != riddle["answer"]:
        print("You have", max_guesses - counter, "guesses left")
        
def add_score(username, score):
    # Add score to leaderboard
    with open("data/leaderboard.txt", "a") as chat_list:
        chat_list.writelines("({0}) {1} - {2}\n".format(
            message_dict["timestamp"], 
            message_dict["from"].title(), 
            message_dict["message"]))
    #messages.append("({}) {}: {}".format(now, username, message)) #brackets act as placeholders for time, user and message


with open("riddles.json") as riddles_file:
    riddles = json.load(riddles_file)

for riddle in riddles: #loops through the quiz questions
    print(quiz(riddle))

