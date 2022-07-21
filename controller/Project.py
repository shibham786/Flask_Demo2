
from config import app
from model.Project import Project

@app.route("/AddProject",methods=['POST'])
def AddProject():
   return Project.AddProject()

@app.route("/getAllProjects",methods=['GET'])
def getAllProjects():
   return Project.getAllProject()