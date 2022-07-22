import json
from unittest import result

from config import db, app
from flask import jsonify, request,abort
from flask_migrate import Migrate
import jwt
from datetime import datetime, timedelta
from model.Project import Project

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    contact = db.Column(db.String(11),unique=True,nullable=False)
    password = db.Column(db.String(50),nullable=False)
    projects = db.relationship('Project', backref='user',cascade="all, delete",lazy='select')

    def __init__(self,username,contact,password):
        self.username = username
        self.contact = contact
        self.password = password

    @classmethod
    def get(self):
        user_list = []
      
        users = User.query.all()
        for user in users:
            result = {
                "userid":user.user_id,
                "username":user.username,
                "contact":user.contact,
                "projects":[{"pid": p.pid,"pname":p.pname} for p in user.projects],
            }
            user_list.append(result)

        return jsonify({
        "success":True,
        "users":user_list,
    })

    @classmethod
    def getProjectByUser(self):
        project_list = []
        users = db.session.query(User).all()
        print(users)
        for u in users:
            print(u.projects.all())
            result = {
                "username":u.username,
                "projects": u.projects.all()

             }
            project_list.append(result)

        print("=============",project_list)

        projects = db.session.query(User).first().projects
        print("project all =========",projects.all())
        return jsonify({
            "projects":[{"pname": p.pname} for p in projects]
        })

    @classmethod
    def AddUser(self):
        user_data = request.json

        username = user_data['username']
        contact = user_data['contact']
        password = user_data['password']

        user = User(username=username,contact=contact,password=password)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            "Success":True,
            "Message":"User Added"
        })

    @classmethod
    def login_User(self):
        user = db.session.query(User).filter(User.username == request.json['username'],User.password ==request.json['password']).first()
        print("========",user.username)
        if user:
            token = jwt.encode({
            'user_id': user.user_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 60)
        }, app.config['SECRET_KEY'], algorithm="HS256")
            decode =  jwt.decode(token,app.config['SECRET_KEY'], algorithms=["HS256"])
            print("decode",decode)
            return jsonify({
            "Success":True,
            "token":token})
       
        else:
            return jsonify({
            "Success":False,
            "Message":"User  not found"})

    @classmethod
    def DeleteUser(self,id):
        user = User.query.get(id)
        if user is None:
            abort(404)
        else:
            db.session.delete(user)
            db.session.commit()
            return jsonify({
                "Success":True,
                "message":"User Deleted success"
            })

    @classmethod
    def UpdateUser(self,id):
        user = User.query.get(id)

        if user is None:
            abort(404)
        else:
            user.username = request.json['username']
            db.session.add(user)
            db.session.commit()

            return jsonify({
                "Success":True,
                "Message":"User Updated"
            })


