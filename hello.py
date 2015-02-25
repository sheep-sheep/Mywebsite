from flask import Flask
app = Flask(__name__)

# @app.route('/') # what URL should trigger our function.
# def hello_world():
#     return 'Hello World! Testing'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/hello/<username>')
def show_user_profile(username = 'yang'):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0')