from os import abort
from config import db

from flask import jsonify, request
from flask_cors import cross_origin


class Project(db.Model):
    pid = db.Column(db.Integer, primary_key=True)  # change name to meaningfull
    pname = db.Column(db.String(50), unique=True, nullable=False)
    desc = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    def __init__(self, pname, desc, user_id):
        self.pname = pname
        self.desc = desc
        self.user_id = user_id

    @classmethod
    def getAllProject(self):
        projects = db.session.query(Project).all()
        return projects

    def AddProject(self):

        db.session.add(self)
        db.session.commit()

    def DeleteProject(self):

        db.session.delete(self)
        db.session.commit()

    def UpdateProject(self):

        db.session.add(self)
        db.session.commit()
