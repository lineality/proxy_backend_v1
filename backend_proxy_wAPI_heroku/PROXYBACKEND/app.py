from decouple import config
from flask import Flask, render_template, request, redirect
from praw import Reddit
from urllib.parse import quote_plus

"""
Usually the url is formatted like this:
baseurl/prediction - it has GET capability
baseurl/user - it has GET/POST capability
baseurl/article  - it has GET/POST/PUT capability

(mod)
baseurl/predictions - it has GET/put capability
baseurl/credentials - it has GET/POST capability (user)
baseurl/article  - it has GET/POST/PUT capability
baseurl/title  - it has GET/POST/PUT capability
baseurl/subreddit_choice  - it has GET/POST capability

plus:
sqlite3 db...
or...pandas.df?
"""

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return render_template("home.html")

    @app.route("/post_to_reddit/<subreddit>/<title>/<article>")
    def predict_subreddit(subreddit, article, title):
        return redirect("https://www.reddit.com/r/{}/submit?text={}&title={}".format(subreddit, (article), quote_plus(title)))

""" additions below here """

    @app.route("/predictions/GET/<>/")
    def prediction_get():
        return

    @app.route("/predictions/POST/<>/")
    def prediction_post():
        return

    @app.route("/credentials/POST/<>/")
    def credentials_post():
        return

    @app.route("/credentials/GET/<>/")
    def credentials_get():
        return

    @app.route("/article/POST/<>/")
    def article_post():
        return

    @app.route("/article/PUT/<>/")
    def article_put():
        return

    @app.route("/article/GET/<>/")
    def article_get():
        return

    @app.route("/title/POST/<>/")
    def title_post():
        return

    @app.route("/title/PUT/<>/")
    def title_put():
        return

    @app.route("/title/GET/<>/")
    def title_get():

    @app.route("/subreddit_choice/GET/<>/")
    def subreddit_choice_get():
        return

    @app.route("/subreddit_choice/POST/<>/")
    def subreddit_choice_post():
        return



    return app
