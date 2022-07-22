
from config import app
from model.Project import Project

@app.route("/AddProject",methods=['POST'])
def AddProject():
   return Project.AddProject()

@app.route("/getAllProjects",methods=['GET'])
def getAllProjects():
   return Project.getAllProject()


@app.route("/DeleteProject/<int:pid>",methods=['DELETE'])
def DeleteProject(pid):
   return Project.DeleteProject(pid)


@app.route("/UpdateProject/<int:pid>",methods=['PATCH'])
def UpdateProject(pid):
   return Project.UpdateProject(pid)