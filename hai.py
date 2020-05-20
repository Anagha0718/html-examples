from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def app():
    return render_template('home.html')
@app.route('/world')
def world():
    return render_template('we.html')
if __name__=='__main__':
    app.run(debug = True,use_reloader = True)
