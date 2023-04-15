from flask import Flask, render_template

app = Flask(__name__)


timer = 25
@app.route('/')
def index():
    return render_template('form.html')


@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/counter', methods = ['POST', 'GET'])
def counter():
    global timer 
    return render_template('index.html', counter=timer)


if __name__ == '__main__':
    app.run()
