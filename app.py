from config import app ,db
from model import User,Project
from controller import User,Project


@app.route("/")
def welcome():
    return "Hello Admin  bhai"

@app.before_first_request
def initfunction():
    db.create_all()
    print('before_first_request')

if __name__ == "__main__":
    app.run(debug=True,port=8000)