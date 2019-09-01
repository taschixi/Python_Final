from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	title = "Homepage"
	return render_template("index.html", title=title)

@app.route('/about')
def about():
	title = "About Today's Image"
	return render_template("about.html", title=title)