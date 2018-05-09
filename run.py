import os
import json
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'some_secret' 

@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", page_title="Home", user=user)
    
@app.route('/')
def user(user):
    return "Hi " + username


@app.route('/leader')
def leader():
    return render_template("leader.html", page_title="Leaderboard")


@app.route('/signUp', methods = ['GET', 'POST'])
def signUp():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.write(request.form["user"])
            user_list.write("\n")
        return redirect(request.form["user"])
    else:
        return render_template("signUp.html")

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

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

with open("data/riddles.json") as riddles_file:
    riddles = json.load(riddles_file)

for riddle in riddles: #loops through the quiz questions
    print(quiz(riddle))