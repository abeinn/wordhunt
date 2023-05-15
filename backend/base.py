from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def profile():
    response_body = {
        "name": "Hi",
        "about": "Hello"    
    }
    return response_body