from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)