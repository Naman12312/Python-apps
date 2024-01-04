from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/admin')
def main():
    return 'This is admin page...'
app.run(debug=True)