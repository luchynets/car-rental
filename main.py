from flask import Flask, render_template, request, redirect, url_for
import os
import save
import datetime


app = Flask(__name__)
save.create()

@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html', posts = save.get())

@app.route('/add', methods = ['GET', 'POST'])
def add():
	if request.method == 'POST':
		with open('now.txt', 'r+') as file:
			id_ = int(file.read())
			file.seek(0)
			file.write(str(id_ + 1))
		f = request.files['photo']
		f.save(f'photo_{id_}.png')
		des = request.form['des']
		price = request.form['price']
		save.add(id_, f'/user_images/photo_{id_}.png', des, price, datetime.date.today().strftime("%Y.%m.%d"))
		return redirect('/succesful')
	return render_template('add.html')

@app.route('/succesful')
def succesful():
	return 'Added succes! <a href="/">Return on main page</a>'

app.run(debug = True)