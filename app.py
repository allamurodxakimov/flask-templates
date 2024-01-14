from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from randomuser import randomusers

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():

    params = request.args

    title = 'Random Users'
    users = randomusers(params['n'], params['gender'])

    return render_template('index.html', context={'title': title, 'users': users})


@app.route('/about')
def about():
    return "Hello about"


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'), port=os.getenv('PORT'))
