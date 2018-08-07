from flask import Flask
from flask import request

tom = Flask(__name__)

@tom.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@tom.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action='/signin' method='post'>
              <p><input name='username'></p>
              <p><input name='password'></p>
              <p><button type='submit'>Sign In</button></p>
              </form>'''

@tom.route('/signin', methods=['POST'])
def signin():
    # require get form from request object
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    tom.run()