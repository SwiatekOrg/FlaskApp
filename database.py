import sqlite3

class DataBase():

	def __init__(self):
		self.conn = None
		self.connect()
		self.cursor = self.get_cursor()
        #self.cursor.execute('''CREATE TABLE stocks
             #(user_id int, username text, password text, email text)''')
		self.conn.commit()
		self.add_account("jd","jd","jd@op.pl")

	def connect(self):
		self.conn = sqlite3.connect('database1.db')

	def get_cursor(self):
		return self.conn.cursor()

	def get_account(self,username):
		self.conn.execute("SELECT * FROM users WHERE username=\"%s\"" % username)
		user = self.cursor.fetchone()
		return user

	def get_user_password(self,username):
		self.conn.execute("SELECT password FROM users WHERE username=\"%s\"" % username)
		password = self.cursor.fetchone()
		return password

	def add_account(self,username,password,email):
		if self.get_account(username) is not None and \
			username in self.get_account(username):
			return False
		self.cursor.execute("INSERT INTO users(username, password, email) VALUES(\"%s\", \"%s\", \"%s\")" % (username, password, email))
		print("Dodano " + username)
		self.conn.commit()
		return True
