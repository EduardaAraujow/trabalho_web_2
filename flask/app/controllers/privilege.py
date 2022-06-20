from app import app, db
from app import Privilege
from flask import request, jsonify

@app.route("/list/privileges",methods=["GET"])
def listar_privilege():
    privileges = Privilege.query.all()
    arr = []
    
    for privilege in privileges:
        arr.append(privilege.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/add/privilege",methods=["POST"])
def adicionar_privilege():
    data = request.get_json()

    if "resource_id" not in data or data["resource_id"] is None:
        return jsonify ({"Error":True, "Message": "resource_id não foi informado"}), 400
    
    if "allow_boolean" not in data or data["allow_boolean"] is None:
        return jsonify ({"Error":True, "Message": "allow_boolean não foi informado"}), 400
    
    if "role_id" not in data or data["role_id"] is None:
        return jsonify ({"Error":True, "Message": "role_id não foi informado"}), 400

    privilege = Privilege()
    privilege.resource_id = data["resource_id"]
    privilege.allow_boolean = data["allow_boolean"]
    privilege.role_id = data["role_id"]
    try:
        db.session.add(privilege)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "Privilege ja existente"})

@app.route("/delete/privilege/<int:role_id>&<int:resource_id>",methods=["DELETE"])
def deletar_privilege(role_id, resource_id):
    privilege = Privilege.filter(role_id==role_id, resource_id==resource_id).first()
    
    if privilege == None:
        return jsonify({"message": "O privilege não existe", "error":True}), 404
    
    db.session.delete(privilege)

    try:
        db.session.commit()
        return jsonify({"message": "Privilege deletado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel deletar o privilege", "error":False}), 200

@app.route("/edit/privilege/<int:role_id>&<int:resource_id>",methods=["PUT"])
def editar_privilege(role_id, resource_id):
    privilege = Privilege.query.filter(role_id==role_id, resource_id==resource_id).first()
    data = request.get_json()

    if privilege == None:
        return jsonify({"message": "O privilege não existe", "error":True}), 404
    
    try:
        if "resource_id" in data:
            privilege.resource_id = data["resource_id"]
        if "allow_boolean" in data:
            privilege.allow_boolean = data["allow_boolean"]
        if "role_id" in data:
            privilege.role_id = data["role_id"]
        db.session.commit()
        return jsonify({"message": "Privilege editado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar o privilege", "error":True}), 200

@app.route("/view/privilege/<int:role_id>&<int:resource_id>",methods=["GET"])
def visualizar_privilege(role_id, resource_id):
    privilege = Privilege.query.filter(role_id==role_id, resource_id==resource_id).first()

    if privilege == None:
        return jsonify({"message": "O privilege não existe", "error":True}), 404
    
    return jsonify({
        "data": privilege.to_dict(),
        "error": False
    })