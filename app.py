from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from command prompt, python, flask, and microsoft azure :)'

if __name__ == '__main__':
    app.run()
