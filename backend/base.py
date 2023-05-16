from flask import Flask, jsonify, request
from word_hunt import solve

api = Flask(__name__)

@api.route('/solve')
def solveWordHunt():

    letters = request.args.get('input_value')
    
    return solve(letters)