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
        self.cursor.execute("SELECT * FROM users WHERE username=\"%s\"" % username)
        user = self.cursor.fetchone()
        return user

    def get_user_username(self,username):
        self.cursor.execute("SELECT username FROM users WHERE username=\"%s\"" % username)
        username = self.cursor.fetchone()
        return username

    def get_user_password(self,username):
        self.cursor.execute("SELECT password FROM users WHERE username=\"%s\"" % username)
        password = self.cursor.fetchone()
        return password

    def login_to_account(self,username,password):
        user = self.get_account(username)
        if str(user[1]) == username and str(user[2]) == password:
            return True
        else:
            return False

    def add_account(self,username,password,email):
        if self.get_user_username(username) is not None:
            return False
        else:
            self.cursor.execute("INSERT INTO users(username, password, email) VALUES(\"%s\", \"%s\", \"%s\")" % (username, password, email))
            self.conn.commit()
            return True
