''' SQLAlchemy models for TwitOff.'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    '''Twitter users that we pull and we analyze tweets for.'''
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.column(DB.BigInteger)

    def __repr__(self):
        return'<User {}>'.format(self.name)


class Tweet(DB.Model):
    '''Tweets.'''
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)

# if __name__=="__main__":
#    DB.create_all()