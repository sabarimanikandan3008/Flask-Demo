from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

@app.route('/about')
def about():
    return 'This is the About Page.'

if __name__ == '__main__':
    app.run(debug=True) 