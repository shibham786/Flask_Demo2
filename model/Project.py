from config import db
from flask import jsonify,request


class Project(db.Model):
    pid = db.Column(db.Integer,primary_key=True)
    pname = db.Column(db.String(50),unique=True,nullable=False)
    desc = db.Column(db.String(50),unique=True,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'),nullable=False)

    def __init__(self,pname,desc,user_id):
        self.pname = pname
        self.desc = desc
        self.user_id = user_id

        

    @classmethod
    def getAllProject(self):
        projects_list = []
        projects = Project.query.all()

        [projects_list.append({"pid":project.pid,"pname":project.pname,"user":project.user_id}) for project in projects]
        return jsonify({
        "success":True,
        "items":projects_list,
    })

    @classmethod
    def AddProject(self):
        project_data = request.json

        pname = project_data['pname']
        desc = project_data['desc']
        user_id = project_data['user_id']

        project = Project(pname=pname,desc=desc,user_id=user_id)
        db.session.add(project)
        db.session.commit()

        return jsonify({
            "Success":True,
            "Message":"Project Added"
        })

