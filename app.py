from config import app, db
from controller import User, Project
from model import User, Pet, Project, Owner


@app.route("/")
def welcome():
    return "Hello Admin  bhai"


@app.before_first_request
def initfunction():
    db.create_all()
    print("before_first_request")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
