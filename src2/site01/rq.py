from flask import Flask, render_template
from flask import request
from urllib.parse import unquote

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/rq/')
def get_request():
	path = request.path
	method = request.method
	name = unquote(request.values['name'])
	return name

@app.route('/reg/')
def reg():
	return render_template('reg.html')

@app.route('/doreg/', methods=['POST', 'GET'])
def do_reg():
	name = request.values['username']
	pwd = request.values['pwd']
	# age = request.args.get('age', 0)
	return '姓名：{}，密码{}'.format(name, pwd)

@app.route('/headers/')
def headers():
	data = dict(request.headers)
	return str(data)

if __name__ == '__main__':
	app.run()