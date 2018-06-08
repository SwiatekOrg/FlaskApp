import sqlite3

class DataBase():

    def __init__(self):
        self.conn = None
        self.connect()
        self.cursor = self.get_cursor()
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

    def get_user_id(self,username):
        self.cursor.execute("SELECT user_id FROM users WHERE username=\"%s\"" % username)
        user_id = self.cursor.fetchone()
        return int(user_id[0])

    def get_user_password(self,username):
        self.cursor.execute("SELECT password FROM users WHERE username=\"%s\"" % username)
        password = self.cursor.fetchone()
        return str(password[0])

    def login_to_account(self,username,password):
        user = self.get_account(username)
        if user == None:
            return False
        elif str(user[1]) == username and str(user[2]) == password:
            return True

    def add_account(self,username,password,email):
        if self.get_user_username(username) is not None:
            return False
        else:
            self.cursor.execute("INSERT INTO users(username, password, email) VALUES(\"%s\", \"%s\", \"%s\")" % (username, password, email))
            self.cursor.execute("INSERT INTO settings(user_id,name,surname,age,sex) VALUES(\"%i\",\"%s\",\"%s\",\"%i\",\"%s\")" % (self.get_user_id(username),"Name","Surname",0,"Sex"))
            self.conn.commit()
            return True

    def change_setting(self,parameter,name,username):
        if type(name) == int:
            self.cursor.execute("UPDATE settings SET \"%s\"=\"%i\" WHERE user_id=\"%i\"" % (parameter,name,self.get_user_id(username)))
        else:
            self.cursor.execute("UPDATE settings SET \"%s\"=\"%s\" WHERE user_id=\"%i\"" % (parameter,name,self.get_user_id(username)))
        self.conn.commit()   

    def change_email(self,newmail,username):   
        self.cursor.execute("UPDATE users SET email=\"%s\" WHERE username=\"%s\"" % (newmail,username))
        self.conn.commit()

    def change_password(self,newpassword,username):
        self.cursor.execute("UPDATE users SET password=\"%s\" WHERE username=\"%s\"" % (newpassword,username))
        self.conn.commit()