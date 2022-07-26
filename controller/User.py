from datetime import datetime, timedelta
from os import abort
from config import app
from model.User import User
from flask import jsonify, request
import jwt


@app.route("/getAllUser", methods=["GET"])
def getAllUsers():
    users = User.get()
    user_list = [
        {
            "userid": user.user_id,
            "username": user.username,
            "password": user.password,
        }
        for user in users
    ]
    return jsonify(
        {
            "status": 200,  # remove this
            "users": user_list,
        }
    )


@app.route("/getProjectByUser", methods=["GET"])
def getProjectByUser():

    users = User.getProjectByUser()
    project_list = []
    for user in users:
        project_list.append(
            {
                "username": user.username,
                "pname": user.pname,
            }
        )
    print("=============", project_list)
    return jsonify({"status": 200, "data": project_list})


@app.route("/AddUser", methods=["POST"])
def AddUser():

    user_data = request.json  # type of data
    print(request.json, type(request.json))
    # read and underzstand the concept of kwargs and args and implement
    # Add validation too
    # change place of code to controller

    # username = user_data["username"]
    # contact = user_data["contact"]
    # password = user_data["password"]

    # error_message = validate_user(user_data)

    # if error_message:
    #     return jsonify({"error": error_message}), 400

    user = User(**user_data)
    user.AddUser()
    return jsonify({"Success": True, "Message": "User Register SuccessFully"})


@app.route("/DeleteUser/<int:id>", methods=["DELETE"])
def DeleteUser(id):
    user = User.query.get(id)
    if user is None:
        return abort(404)

    user.DeleteUsers()
    return jsonify({"Success": True, "message": "User Deleted success"})


@app.route("/UpdateUser/<int:id>", methods=["PATCH"])
def UpdateUser(id):
    user = User.query.get(id)

    if user is None:
        abort(404)
    else:
        user.username = request.json["username"]
        user.UpdateUser()
        return jsonify({"Success": True, "Message": "User Updated"})


@app.route("/login_User", methods=["POST"])
def login_User():
    user = User.login_User(
        username=request.json["username"], password=request.json["password"]
    )

    print(type(user))
    if user:
        token = jwt.encode(
            {
                "user_id": user.username,
                "exp": datetime.utcnow() + timedelta(minutes=60),
            },
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        # decode = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        # print("decode", decode)
        return jsonify({"status": 200, "token": token})

    else:
        return jsonify({"status": 404, "Message": "User  not found"})
