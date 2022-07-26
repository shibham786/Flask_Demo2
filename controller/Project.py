from flask import jsonify, request, abort
from sqlalchemy import true
from config import app
from model.Project import Project
import re


def validation_project_detail(pname: str, desc: str):
    print(not re.match(r"^[A-Za-z]+$", pname))
    print("=====", not re.match(r"^[A-Za-z]+$", desc), len(desc))
    if not re.match(r"^[A-Za-z]+$", pname):
        return "name only contain alphabets"
    if re.match(r"^[A-Za-z]+$", desc) and len(desc) <= 10:
        return "description only contain alphabets and must have 10 characters"


@app.route("/add_projects", methods=["POST"])
def AddProject():
    project_data = request.json

    pname = project_data["pname"]
    desc = project_data["desc"]
    validate = validation_project_detail(pname, desc)
    print("validate", validate)
    if not validate:
        project = Project(**project_data)
        project.AddProject()
        return jsonify({"message": "Project Added"}), 200
    else:
        return jsonify(validate)

    # user_id = project_data["user_id"]


@app.route("/getAllProjects", methods=["GET"])
def getAllProjects():
    projects_list = []
    projects = Project.getAllProject()
    for project in projects:
        projects_list.append(
            {
                "pid": project.pid,
                "pname": project.pname,
                "desc": project.desc,
                "userid": project.user_id,
            }
        )
    return jsonify(
        {
            "status": 200,
            "projects": projects_list,
        }
    )


@app.route("/DeleteProject/<int:pid>", methods=["DELETE"])
def DeleteProject(pid):
    project = Project.query.get(pid)
    if project:

        project.DeleteProject()
        return jsonify({"message": "project deleted"})
    else:
        return jsonify({"message": "data not found"})


@app.route("/UpdateProject/<int:pid>", methods=["PATCH"])
def UpdateProject(pid):
    project = Project.query.get(pid)

    if project is None:
        abort(404)
    else:
        project.pname = request.json["pname"]
        project.desc = request.json["desc"]
        project.UpdateProject()
        return jsonify({"Success": True, "Message": "Project Updated"})
