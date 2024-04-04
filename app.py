from flask import Flask, request, jsonify

from wordle import getWord, makeBoard, contains, updateBoard
app = Flask(__name__)

@app.route('/startGame', methods=['GET'])
def startGame():
    roundWord = getWord()
    board = makeBoard(roundWord)
    return jsonify({'roundWord': roundWord, 'board':board})

