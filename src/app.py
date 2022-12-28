from flask import Flask, render_template, request, redirect, url_for
from Zombie import Zombie
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('zombies/zombies.jinja', zombie=Zombie(True))

@app.route('/zombie')
def zombie():

	fullBody: bool = request.args.get('fullBody')

	return render_template('zombies/zombies.jinja', zombie=Zombie(fullBody))

@app.route('/zombies/<n>')
def zombies(n):

	fullBody: bool = request.args.get('fullBody')

	zombies: list[Zombie] = [ Zombie(fullBody) for _ in range(int(n)) ]

	return render_template('zombies/zombies.jinja', zombies=zombies)

@app.errorhandler(404)
def page_not_found(e):
	return redirect(url_for('zombie'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
