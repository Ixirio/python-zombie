from flask import Flask, render_template, request, redirect, url_for
from Zombie import Zombie
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('zombies/zombies.jinja', zombie=Zombie(True))

def getFullBody(requestArgs) -> bool:
	return True if requestArgs.get('full') == '1' else False

def getRotate(requestArgs) -> bool:
	return True if requestArgs.get('rotate') == '1' else False

@app.route('/zombie')
def zombie():
	return render_template(
		'zombies/zombies.jinja',
		zombies=[ Zombie(getFullBody(request.args)) ],
		rotate=getRotate(request.args)
	)

@app.route('/zombies/<n>')
def zombies(n):
	return render_template(
		'zombies/zombies.jinja',
		zombies=[ Zombie(getFullBody(request.args)) for _ in range(int(n)) ],
		rotate=getRotate(request.args)
	)

@app.errorhandler(404)
def page_not_found(e):
	return redirect(url_for('zombie'))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
