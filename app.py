from flask import Flask, session, redirect, url_for, request, render_template, flash
from database import DataBase
from profile import Profile

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
	username = session['username']
	db = DataBase()
	profile = Profile(db.get_user_id(username))
	if request.method == 'POST':
		username = session['username']
		if 'ProfileData' in request.form:
			name = request.form.get('name')
			surname = request.form.get('surname')
			age = request.form.get('age')
			sex = request.form.get('sex')
			if name != "":
				db.change_setting("name",name,username)
			if surname != "":
				db.change_setting("surname",surname,username)
			if age != "":
				db.change_setting("age",age,username)
			if sex != "":
				db.change_setting("sex",sex,username)
		if 'ChangeMail' in request.form:
			newmail = request.form['email']
			db.change_email(newmail,username)
		return redirect(url_for('settings'))

	return render_template('settings.html', profile = profile)

#@app.route('/profiledata',methods=['GET','POST'])
#def profiledata():

if __name__ == '__main__':
	app.secret_key = "jdu7x3j8e83iej7eeh8e"
	app.run(port=5011)