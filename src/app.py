from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('socle/base.jinja')

@app.route('/zombie')
def zombie():
	return render_template('zombies/zombies.jinja', zombie=1)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
