from config import db


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # change name to meaningfull
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    pets = db.relationship("Pet", backref="owner")
