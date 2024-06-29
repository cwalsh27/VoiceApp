from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm, UploadFileForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'
app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/appone', methods=['GET', "POST"])
def appone():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  #retrieves the file data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename("micropheno_input_text.txt"))) #saves the files
        return "File has been uploaded."

    return render_template('appone.html', form=form)

if __name__ == '__main__': 
    app.run(debug=True)

