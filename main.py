from flask import Flask
from app import views

app = Flask(__name__)

#url
app.add_url_rule("/", 'home', views.homepage)
app.add_url_rule("/gender_recognition", 'gender_recognition', views.gender_recognition, methods=['GET', 'POST'])

#run
if __name__ == "__main__":
	app.run(debug=True)