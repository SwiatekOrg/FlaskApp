from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from database import DataBase

db = DataBase()
app = Flask(__name__)
app.secret_key = "jdu7x3j8e83iej7eeh8e"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == "test" and request.form['password'] == "haslo":
            session['logged_in'] = True
            flash("You were successfully logged in")
            return render_template('index.html')
        else:
            session['logged_in'] = False
            flash("You typed wrong username or password!")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash("You were successfully registered")
        return render_template('register.html')
    else:
        return render_template('register.html')


@app.route('/logout',methods=['GET'])
def logut():
    session['logged_in'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = "jdu7x3j8e83iej7eeh8e"
    app.run(port=5011)