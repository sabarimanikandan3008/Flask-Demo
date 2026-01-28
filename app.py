from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

@app.route('/about', methods=['POST'])
def about():
    if request.method == 'POST':
        name=request.form.get('name')
        return f'Hello, {name}! This is the About Page.'

if __name__ == '__main__':
    app.run(debug=True) 