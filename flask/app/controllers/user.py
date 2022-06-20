from app import app, db
from app import User
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/list/users",methods=["GET"])
def listar_usuarios():
    users = User.query.all()
    arr = []
    
    for user in users:
        arr.append(user.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/add/user",methods=["POST"])
def adicionar_user():
    data = request.get_json()

    if "email" not in data or data["email"] is None:
        return jsonify ({"Error":True, "Message": "email não foi informado"}), 400
    
    if "password" not in data or data["password"] is None:
        return jsonify ({"Error":True, "Message": "password não foi informado"}), 400
    
    if "role_id" not in data or data["role_id"] is None:
        return jsonify ({"Error":True, "Message": "role id não foi informado"}), 400

    user = User()
    user.email = data["email"]
    user.password = generate_password_hash(data["password"], method='sha256')
    user.role_id = data["role_id"]
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "Usuario ja existente"})

@app.route("/delete/user/<int:id>",methods=["DELETE"])
def deletar_user(id):
    user = User.query.get(id)
    
    if user == None:
        return jsonify({"message": "O usuario não existe", "error":True}), 404
    
    db.session.delete(user)

    try:
        db.session.commit()
        return jsonify({"message": "Usuario deletado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel deletar o usuario", "error":False}), 200

@app.route("/edit/user/<int:id>",methods=["PUT"])
def editar_aluno(id):
    user = User.query.get(id)
    data = request.get_json()

    if user == None:
        return jsonify({"message": "O usuario não existe", "error":True}), 404
    
    try:
        if "email" in data:
            user.email = data["email"]
        if "password" in data:
            user.password = data["password"]
        if "role_id" in data:
            user.role_id = data["role_id"]
        db.session.commit()
        return jsonify({"message": "Usuario editado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar usuario", "error":True}), 200

@app.route("/view/user/<int:id>",methods=["GET"])
def visualizar_user(id):
    user = User.query.get(id)

    if user == None:
        return jsonify({"message": "O user não existe", "error":True}), 404
    
    return jsonify({
        "data": user.to_dict(),
        "error": False
    })