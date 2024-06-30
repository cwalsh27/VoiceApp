from flask import Flask, render_template, url_for, flash, redirect, send_from_directory, send_file
from forms import RegistrationForm, LoginForm, UploadDocForm
from werkzeug.utils import secure_filename
from MicrophenoTextProcessor import check_valid_run, process_doc
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
        #file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename('micropheno_input_text.docx'))) 
        flash(f'Succesfully uploaded file named {file.name}!', 'success')

        newFile = process_doc(file)
        newFile.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename('micropheno_output_text.docx'))) 
        return redirect(url_for('download_file', filename='micropheno_output_text.docx'))
    elif form.is_submitted(): 
        flash('Upload Unsuccessful. Please confirm that you are attempting to upload a text file of type .docx', 'danger')

    return render_template('appone.html', form=form, title="Micropheno")

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    # @app.after_request
    # def delete(response):
    #     os.remove()
    
    

if __name__ == '__main__': 
    app.run(debug=True)

