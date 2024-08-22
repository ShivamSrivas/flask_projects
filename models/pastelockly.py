from app import db

class PasteLockly_(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    encrypt_key = db.Column(db.String(255))
    data_time = db.Column(db.DateTime, nullable=False) 

    def __init__(self, text, encrypt_key,data_time):
        self.text = text
        self.encrypt_key = encrypt_key
        self.data_time = data_time 
        
    def __repr__(self):
        return f'<PasteLockly {self.text}>'