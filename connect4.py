import os
from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'secret_key'

ROWS, COLS = 6, 7

def initialize_board():
    return [['O' for _ in range(COLS)] for _ in range(ROWS)]

def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == 'O':
            row[col] = player
            return True
    return False

def check_win(board, player):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    return False

def check_full(board):
    return all(cell != 'O' for row in board for cell in row)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    session['board'] = initialize_board()
    session['player'] = '1'
    session['game_won'] = False
    return redirect(url_for('game'))

@app.route('/game')
def game():
    board = session.get('board', initialize_board())
    player = session.get('player', '1')
    game_won = session.get('game_won', False)
    return render_template('game.html', board=board, player=player, game_won=game_won)

@app.route('/make_move/<int:col>', methods=['POST'])
def make_move_route(col):
    board = session.get('board', initialize_board())
    player = session.get('player', '1')
    if make_move(board, col, player):
        session['board'] = board
        if check_win(board, player):
            session['game_won'] = True
        elif check_full(board):
            session['game_won'] = True
        else:
            session['player'] = '2' if player == '1' else '1'
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True)
