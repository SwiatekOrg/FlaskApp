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
