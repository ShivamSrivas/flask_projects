from app import db

class ShortenURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    shortened_url = db.Column(db.String(255), unique=True, nullable=False)
    redirect_options = db.Column(db.String(255))
    link_length = db.Column(db.Integer)
    data_time = db.Column(db.DateTime, nullable=False) 

    def __init__(self, original_url, shortened_url, redirect_options, link_length, data_time):
        self.original_url = original_url
        self.shortened_url = shortened_url
        self.redirect_options = redirect_options
        self.link_length = link_length
        self.data_time = data_time

    def __repr__(self):
        return f'<ShortenURL {self.original_url}>'