from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World! I am a website! Pretty cool huh?"

app.run(debug=True)