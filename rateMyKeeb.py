from flask import Flask, redirect, url_for, render_template
import reddit_data

app = Flask(__name__) 
@app.route("/")
def home_page():
    submission_limit = 10
    instance = reddit_data.reddit_instance()
    submissions = instance.subreddit("customkeyboards").new(limit=submission_limit)
    return render_template('index.html', data = list(map(reddit_data.get_submission_data, submissions)))

# Error page
@app.errorhandler(404)
def no_page(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)
