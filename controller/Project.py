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
    if not re.match(r"^[A-Za-z]+$", desc):
        return "description only contain alphabets"
    if len(desc) <= 10:
        return "description must be greater than 10 character"


@app.route("/add_projects", methods=["POST"])
def AddProject():
    project_data = request.json

    pname = project_data["pname"]
    desc = project_data["desc"]
    validate = validation_project_detail(pname, desc)

    if not validate:
        project = Project(**project_data)
        project.AddProject()
        return jsonify({"message": "Project Added"}), 200
    else:
        return jsonify(validate)


@app.route("/get_all_projects", methods=["GET"])
def getAllProjects():
    projects_list = []
    projects = Project.getAllProject()

    [
        projects_list.append(
            {"pid": project.pid, "pname": project.pname, "desc": project.desc}
        )
        for project in projects
    ]
    return (
        jsonify(
            {
                "projects": projects_list,
            }
        ),
        200,
    )


@app.route("/delete_project/<int:pid>", methods=["DELETE"])
def DeleteProject(pid):
    project = Project.query.get(pid)
    if project:

        project.DeleteProject()
        return jsonify({"message": "project deleted"}), 200
    else:
        return jsonify({"message": "data not found"}), 404


@app.route("/update_project/<int:pid>", methods=["PATCH"])
def UpdateProject(pid):
    project = Project.query.get(pid)

    if project is None:
        abort(404)
    else:
        validate = validation_project_detail(
            request.json["pname"], request.json["desc"]
        )
        if not validate:
            project.pname = request.json["pname"]
            project.desc = request.json["desc"]
            project.UpdateProject()
            return jsonify({"Message": "Project Updated"}), 200
        else:
            return jsonify(validate), 400
