from flask import jsonify
from config import db, app

# from flask import jsonify, request, abort
import json
from datetime import datetime, timedelta
from flask_cors import cross_origin

from model.Project import Project

# users = (
#     db.session.query(User, Project)
#     .join(Project, User.user_id == Project.user_id)
#     .with_entities(User.username, Project.pname)
#     .all()
# )

# with_entities, loads_only
# Join use (Example of outer join)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    projects = db.relationship(
        "Project", backref="user", cascade="all, delete", lazy="select"
    )

    def __init__(self, username, contact, password):
        self.username = username
        self.contact = contact
        self.password = password

    @classmethod
    def get(self):

        users = User.query.all()
        return users

    def AddUser(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getProjectByUser(self):

        users = (
            db.session.query(User)
            .join(Project)
            .with_entities(User.username, Project.pname, Project.desc)
        )

        print(users)
        return users

    @classmethod
    def login_User(self, username, password):
        user = self.query.filter(
            self.username == username,
            self.password == password,
        ).first()
        print(user)
        return user

    def DeleteUsers(self):
        db.session.delete(self)
        db.session.commit()

    def UpdateUser(self):

        db.session.add(self)
        db.session.commit()
