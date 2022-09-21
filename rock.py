from flask import Flask, render_template
from random import randint

app = Flask(__name__)

def computer_move():
    options = ['Rock','Papper','Scissor']
    move = options[randint(0,2)]
    return move

def winner(computer_move,player_move):
    if computer_move == player_move:
        winner = 'tie'
    elif player_move == 'Rock' and computer_move == 'Papper':
        winner = 'computer'
    elif player_move == 'Papper' and computer_move == 'Scissor':
        winner = 'computer'
    elif player_move == 'Scissor' and computer_move == 'Rock':
        winner = 'computer'
    else:
        winner = 'player'
    return winner




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pathu/<choice>')
def pathu(choice):
    player_move = choice
    computer = computer_move()
    winner_g = winner(computer,player_move)
    print(winner_g)
    return render_template('winner.html',pathu = winner_g,computer =computer,player_move= player_move)

if __name__ =="__main__":
    app.run()
