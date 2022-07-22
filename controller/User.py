
from config import app
from model.User import User

@app.route("/getAllUser",methods=['GET'])
def getAllUsers():
    return User.get()

@app.route("/getProjectByUser",methods=['GET'])
def getProjectByUser():
    return User.getProjectByUser()

@app.route("/AddUser",methods=['POST'])
def AddUser():
    return User.AddUser()

@app.route("/DeleteUser/<int:id>",methods=['DELETE'])
def DeleteUser(id):
    return User.DeleteUser(id)

@app.route("/UpdateUser/<int:id>",methods=['PATCH'])
def UpdateUser(id):
    return User.UpdateUser(id)

@app.route("/login_User",methods=['POST'])
def login_User():
    return User.login_User()



