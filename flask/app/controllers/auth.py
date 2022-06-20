from flask import Flask, jsonify, request
from app import app, db
from app import User
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
import json
import jwt
import datetime

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    if "email" not in data or data["email"] is None:
        return jsonify ({"Error":True, "Message": "email não foi informado"}), 400

    if "password" not in data or data["password"] is None:
        return jsonify ({"Error":True, "Message": "password não foi informado"}), 400
    
    user = User.query.filter_by(email=data["email"]).first()
    if user is None:
        return jsonify ({"Error":True, "Message":"Usuario não existe"})
    
    if (check_password_hash(user.password, data["password"])) == False:
        return jsonify ({"message":"Senha incorreta"})

    access_token = create_access_token(identity=user.email)
    refresh_token = create_refresh_token(identity=user.email)
    
    return jsonify({"access_token":access_token, "refresh_token":refresh_token, "messsage":"Token de acesso gerado com sucesso"})

@app.route("/me", methods=["GET"])
def me():
    return jsonify ({"message":"oi"})

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
