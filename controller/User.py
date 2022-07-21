
from config import app
from model.User import User

@app.route("/getAllUser",methods=['GET'])
def getAllUsers():
    return User.get()

@app.route("/AddUser",methods=['POST'])
def AddUser():
    return User.AddUser()


