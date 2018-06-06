from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  print('yo')
  return render_template('hello.html')