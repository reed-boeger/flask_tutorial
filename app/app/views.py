from app import app

from flask import render_template



@app.route("/")
def index():
    return render_template('/public/index.html')

@app.route("/public/jinja")
def jinja():

    my_name = "Reed"

    return render_template('/public/jinja.html', my_name=my_name)

@app.route("/public/about")
def about():
    return render_template('/public/about.html')
    # return "<h1 style='color: red'>About!!!!</h1>"