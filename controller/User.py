
from config import app
from model.User import User

@app.route("/getAllUser",methods=['GET'])
def getAllUsers():
    return User.get()

@app.route("/AddUser",methods=['POST'])
def AddUser():
    return User.AddUser()

@app.route("/DeleteUser/<int:id>",methods=['DELETE'])
def DeleteUser(id):
    return User.DeleteUser(id)


