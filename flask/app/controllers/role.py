from app import app, db
from app import Role
from flask import request, jsonify

@app.route("/list/role",methods=["GET"])
def listar_role():
    roles = Role.query.all()
    arr = []
    
    for role in roles:
        arr.append(role.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/add/role",methods=["POST"])
def adicionar_role():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify ({"Error":True, "Message": "nome não foi informado"}), 400
    
    role = Role()
    role.name = data["name"]
    try:
        db.session.add(role)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "Role ja existente"})

@app.route("/delete/role/<int:id>",methods=["DELETE"])
def deletar_role(id):
    role = Role.query.get(id)
    
    if role == None:
        return jsonify({"message": "O role não existe", "error":True}), 404
    
    db.session.delete(role)

    try:
        db.session.commit()
        return jsonify({"message": "Role deletado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel role o usuario", "error":False}), 200

@app.route("/edit/role/<int:id>",methods=["PUT"])
def editar_role(id):
    role = Role.query.get(id)
    data = request.get_json()

    if role == None:
        return jsonify({"message": "O usuario não existe", "error":True}), 404
    
    try:
        if "name" in data:
            role.name = data["name"]

        db.session.commit()
        return jsonify({"message": "Role editado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar role", "error":True}), 200

@app.route("/view/role/<int:id>",methods=["GET"])
def visualizar_role(id):
    role = Role.query.get(id)

    if role == None:
        return jsonify({"message": "O role não existe", "error":True}), 404
    
    return jsonify({
        "data": role.to_dict(),
        "error": False
    })