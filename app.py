from flask import Flask, render_template
from dotenv import load_dotenv
import os


app = Flask(__name__)

@app.route('/')
def home():

    title = 'Bosh Sahifa'

    return render_template('index.html', context={'title': title})


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'), port=os.getenv('PORT'))
