from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This a test web application for Devops Training,go devops</h1>"

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True)