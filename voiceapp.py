from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "hello world"

@app.route('/about')
def about():
    return "this is the about page"

if __name__ == '__main__': 
    app.run(debug=True)

