from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello cse'
if __name__=='main_':
    app.run(debug=True, host='0.0.0.0')
