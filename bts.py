from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return"<body bgcolor='yellow' text='blue'><h1>This is Ishita</h1></body>"