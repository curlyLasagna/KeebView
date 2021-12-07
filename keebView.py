from flask import Flask, render_template
from dotenv import load_dotenv
import sys
import logging
import reddit_data as rd

load_dotenv()
app = Flask(__name__) 
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route("/")
def home_page(methods=["GET"]):
    return render_template('index.html', data = rd.get_data(submission_limit = 10))

# Error page
@app.errorhandler(404)
def no_page(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run()
