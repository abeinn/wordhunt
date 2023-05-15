from flask import Flask

api = Flask(__name__)

@api.route('/data')
def profile():
    response_body = {
        'Name':"geek", 
        "Age":22,
        "Date":"5", 
        "programming":"python"    
    }
    return response_body