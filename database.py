import sqlite3

class DataBase():

	def __init__(self):
		self.conn = None
		self.connect()
		self.cursor = self.get_cursor()
        #self.cursor.execute('''CREATE TABLE stocks
             #(user_id int, username text, password text, email text)''')
		self.conn.commit()

	def connect(self):
		self.conn = sqlite3.connect('database1.db')

	def get_cursor(self):
		return self.conn.cursor()

	def get_account(self,username):
		self.conn.execute("SELECT * FROM users WHERE username=\"%s\"" % username)
		user = self.cursor.fetchone()
		print(self.cursor.description)
		print("wartisc cursor.fetchone()" + str(user))
		return user

	def get_user_password(self,username):
		self.conn.execute("SELECT password FROM users WHERE username=\"%s\"" % username)
		password = self.cursor.fetchone()
		return password

	def add_account(self,username,password,email):
		print("funkcja get account daje "+ str(self.get_account(username)))
		if self.get_account(username) is not None:
			return False
		else:
			self.cursor.execute("INSERT INTO users(username, password, email) VALUES(\"%s\", \"%s\", \"%s\")" % (username, password, email))
			self.conn.commit()
			return True
