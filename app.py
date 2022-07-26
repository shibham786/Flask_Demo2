from config import app ,db
from controller import User,Project


@app.route("/")
def welcome():
    return "Hello Admin  bhai"

if __name__ == "__main__":
    app.run(debug=True,port=8000)