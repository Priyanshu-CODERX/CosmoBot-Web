from flask import Flask, render_template, request
from CosmoBot import bot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		doubt_input = request.form['doubt']
		res = bot(doubt_input)
		return render_template('index.html', doubt_input = res)


if __name__ == '__main__':
	app.run(port='8080', debug=True)