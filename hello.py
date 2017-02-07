from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello_world():
	return 'Hello World!'

@app.route('/user/<username>')
def show_username(username):
	return 'User is %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post ID is %d' % post_id

@app.route('/pagelist')
def show_url():
	url = '<a href="http://127.0.0.1:5000/' + url_for('hello_world') + '">hello_world</a>'
	return url_for('hello_world')

if __name__ == '__main__':
	app.run(debug = True)