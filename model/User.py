import json
from os import abort
from config import db
from flask import jsonify, request

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    contact = db.Column(db.String(11),unique=True,nullable=False)
    projects = db.relationship('Project', backref='user',cascade="all, delete")

    def __init__(self,username,contact):
        self.username = username
        self.contact = contact

    @classmethod
    def get(self):
        user_list = []
      
        users = User.query.all()
        for user in users:
            # for p in user.projects:
            #     print(p.pid)
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
    def AddUser(self):
        user_data = request.json

        username = user_data['username']
        contact = user_data['contact']

        user = User(username=username,contact=contact)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            "Success":True,
            "Message":"User Added"
        })

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

