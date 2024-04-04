from flask import Flask, request, jsonify

from wordle import getWord, makeBoard, contains, updateBoard
app = Flask(__name__)

@app.route('/startGame', methods=['GET'])
def startGame():
    return "Hello World!"