from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Game settings
ROWS = 6
COLS = 7
board = [['O' for _ in range(COLS)] for _ in range(ROWS)]
current_player = 'R'  # 'R' for Red, 'Y' for Yellow

def check_win(board, player):
    # Check horizontal, vertical, and diagonal win conditions
    pass

@app.route('/')
def index():
    ROWS = 6
    COLS = 7
    return render_template('index.html', ROWS=ROWS, COLS=COLS)

@app.route('/move', methods=['POST'])
def make_move():
    global current_player
    col = request.json['col']
    # Place the player's disk in the board
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 'O':
            board[row][col] = current_player
            break

    # Check for win or draw
    if check_win(board, current_player):
        return jsonify({'status': 'win', 'player': current_player})

    current_player = 'Y' if current_player == 'R' else 'R'
    return jsonify({'status': 'continue', 'player': current_player, 'board': board})

if __name__ == '__main__':
    app.run(debug=True)
