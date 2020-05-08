from flask import Flask
from flask import Flask, flash, render_template, request, session
app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged.in'):
        return render_template('login.html')
    else:
        return "hello welcome"

@app.route('/login' , methods = ['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'username':
        session['logged_in'] = True
    else:
        flash('wrong passeword')
        return home()
        
