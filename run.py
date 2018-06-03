import os
import json
from flask import Flask, render_template, redirect, request

riddles=[]
with open("data/riddles.json") as riddles_file:
    riddles = json.load(riddles_file)

app = Flask(__name__)
app.secret_key = 'some_secret' 

@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/<user>', methods = ['GET', 'POST'])
def quiz(user):
    
    riddle = riddles[0]

    def right_answer(answer, riddle):
        if answer == riddle("answer"):
            game_status[user] += 1
            print("Well done. You are correct!")
        else:
            print("Sorry you are incorrect. Try again")

    if request.method == "POST":
        answer = request.form["answer"]
        
        
    return render_template("user.html", user=user, score=game_status[user], question=riddle["question"] )
    
    
@app.route('/leader')
def leader():
    return render_template("leader.html", page_title="Leaderboard")

# Log user in on entry of username. If unsuccessful show sign in page again
@app.route('/signUp', methods = ['GET', 'POST'])
def signUp():
    if request.method == "POST":
        user = request.form["user"] #user variable asks for username from the form
        game_status[user] = 0 #sets users score to 0
        return redirect(user) #redirect user (to quiz page)
    else:
        return render_template("signUp.html")

game_status = {
  'user': 0,
}
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
