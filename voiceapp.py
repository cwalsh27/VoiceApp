from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, UploadDocForm
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
    form = UploadDocForm()
    if form.validate_on_submit():
        file = form.file.data  #retrieves the file data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename('micropheno_input_text.docx'))) #saves the files
        flash(f'Succesfully uploaded file named {file.name}!', 'success')
    #else: 
        #flash('Upload Unsuccessful. Please confirm that you are attempting to upload a text file of type .docx', 'danger')
    return render_template('appone.html', form=form)

if __name__ == '__main__': 
    app.run(debug=True)

