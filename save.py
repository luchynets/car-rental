import os
import sqlite3


def create():
	conn = sqlite3.connect("database.db") #Connect database
	cursor = conn.cursor()
	#Create table
	cursor.execute("""CREATE TABLE IF NOT EXISTS posts
		                  (id int, `text` varchar, photo varchar, price varchar,
		                   `date` varchar)
		            """)
	conn.close()

def replace(id_):
	os.replace(f'photo_{id_}.png', f'static/user_images/photo_{id_}.png')

def add(id_, photo, description, price, date):
	replace(id_)
	conn = sqlite3.connect("database.db") #Connect database
	cursor = conn.cursor()
	params = (id_, description, photo, price, date)
	cursor.execute("""INSERT INTO posts VALUES (?, ?, ?, ?, ?)""", params)
	conn.commit()
	conn.close()

def get():
	conn = sqlite3.connect("database.db") #Connect database
	cursor = conn.cursor()
	cursor.execute("""SELECT * FROM posts""")
	data = cursor.fetchall()
	conn.close()
	return data

