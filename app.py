from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from database import DataBase

app = Flask(__name__)
app.secret_key = "jdu7x3j8e83iej7eeh8e"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	db = DataBase()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if db.login_to_account(username,password):
			session['logged_in'] = True
			session['username'] = request.form['username']
			return render_template('index.html')
		else:
			session['logged_in'] = False
			flash("You typed wrong username or password!")
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	db = DataBase()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		if db.add_account(username,password,email):
			flash("You were successfully registered!")
			return render_template('register.html')
		else:
			flash("That user arleady exist")
			return render_template('register.html')
	return render_template('register.html')


@app.route('/logout',methods=['GET'])
def logut():
	session['logged_in'] = False
	return redirect(url_for('index'))

@app.route('/settings',methods=['GET','POST'])
def settings():
	db = DataBase()
	if request.method == 'POST':
		name = request.form['name']
		surname = request.form.get('surname')
		age = request.form.get('age')
		sex = request.form.get('sex')
		username = session['username']
		print(username)
		db.change_name(name,username)
	return render_template('settings.html')

#@app.route('/profiledata',methods=['GET','POST'])
#def profiledata():

if __name__ == '__main__':
	app.secret_key = "jdu7x3j8e83iej7eeh8e"
	app.run(port=5011)