from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>WELCOME TO FLASK</h1>'

@app.route('/')
def 



app.run(debug=True)