import os
import json
from flask import Flask, flash, render_template, redirect, request

riddles=[]
with open("data/riddles.json") as riddles_file:
    riddles = json.load(riddles_file)

    
def right_answer(answer, riddle):
    return answer == riddle["answer"]
    
def wrong_answer(answer, riddle):
    return answer != riddle["answer"]


app = Flask(__name__)
app.secret_key = 'some_secret' 

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/broken')
def fail():
    assert 1 == 2
    

@app.route('/<user>', methods = ['GET', 'POST'])
def quiz(user):
    
    riddle = riddles[0]
    

    if request.method == "POST":
        answer = request.form.get("answer")
        
        if right_answer(answer, riddle):
            game_status[user] += 1
            return render_template("user.html", user=user, score=game_status[user], question=riddle["question"], message = "Correct. Well done!")
            
        else:
            return render_template("user.html", user=user, score=game_status[user], question=riddle["question"], message = "This is wrong. Try again")
            
        # check that the answer is correct.
        # If true, display success message
        # Add score
        # Move to next question.
        # If false, display wrong message
        # Reduce no of guesses counter
        # Show question again
        
    return render_template("user.html", user=user, score=game_status[user], question=riddle["question"] )
    
    
@app.route('/leader')
def leader():
    return render_template("leader.html", page_title="Leaderboard")

# Log user in on entry of username. If unsuccessful show sign in page again
@app.route('/signUp', methods = ['GET', 'POST'])
def signUp():
    if request.method == "POST":
        user = request.form["user"]
        game_status[user] = 0
        return redirect(user)
    else:
        return render_template("signUp.html")

#dictionary with user value and 3 values within it. USe this to keep track of a users progress
game_status = {
  "mark": {
    "score": 3,
    "attempts": 2,
    "riddle": 5,
  }
}
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
