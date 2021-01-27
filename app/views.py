from flask import render_template, request
from flask import redirect, url_for
import os

Upload_folder = 'static/upload'

def homepage():
	return render_template("homepage.html")

def gender_recognition():
	if request.method == 'POST':
		file = request.files['image']
		filename = file.filename
		path = os.path.join(Upload_folder, filename)
		file.save(path)
		return render_template("gender_recognition.html", fileupload=True, img_name=filename)

	return render_template("gender_recognition.html", fileupload=False, img_name=None)
