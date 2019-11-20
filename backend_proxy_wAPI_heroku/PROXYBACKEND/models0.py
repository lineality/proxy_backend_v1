"""
These are my database models
lets make this a relational database

one tweet to many users
These are my database models
"""


from flask_sqlalchemy import SQLAlchemy

#import database. capital for global scope
DB = SQLAlchemy()

"""
class User(DB.Model):
    #  users that we analyze
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '<User {}>'.format(self.name)
"""

class post_here_datatable(DB.Model):
    """The user's data in a table"""
    user_id = DB.Column(DB.BigInteger, primary_key=True)
    user_name = DB.Column(DB.Unicode(300))
    article_text = DB.Column(DB.Unicode(300))
    article_title = DB.Column(DB.Unicode(300))
    recommendations = DB.Column(DB.Unicode(300))

    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    embedding = DB.Column(DB.PickleType, nullable=False)

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
