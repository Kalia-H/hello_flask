from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello from command prompt, python, flask, and microsoft azure :)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
