from flask import Flask, redirect, url_for, render_template
import reddit_data as rd
import os

app = Flask(__name__) 
@app.route("/")
def home_page():
    return render_template('index.html', data = rd.get_data(submission_limit = 10))

# Error page
@app.errorhandler(404)
def no_page(e):
    return render_template("404.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, port = port, host='0.0.0.0')