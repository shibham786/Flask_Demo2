from config import db
#only for checking backref work or not bakref dene pr owner se pet and pet se owner access hota hai bt uss time contrcutor use ni kiya 
# maine toh ho rha hai bt construcotr dalne pr error

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # change name to meaningfull
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"))
