from app import app, db
from app import Resource
from flask import request, jsonify

@app.route("/list/resources",methods=["GET"])
def listar_resources():
    resources = Resource.query.all()
    arr = []
    
    for resource in resources:
        arr.append(resource.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/add/resource",methods=["POST"])
def adicionar_resource():
    data = request.get_json()

    if ("action_id" not in data or data["action_id"] is None) and ("controller_id" not in data or data["controller_id"] is None):
        return jsonify ({"Error":True, "Message": "Controller_id não foi informado"}), 400

    if "action_id" not in data or data["action_id"] is None:
        return jsonify ({"Error":True, "Message": "action_id não foi informado"}), 400
    
    if "controller_id" not in data or data["controller_id"] is None:
        return jsonify ({"Error":True, "Message": "controller_id não foi informado"}), 400

    resource = Resource()
    resource.action_id = data["action_id"]
    resource.controller_id = data["controller_id"]

    try:
        db.session.add(resource)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "Resource ja existente"})

@app.route("/delete/resource/<int:id>",methods=["DELETE"])
def deletar_resource(id):
    resource = Resource.query.get(id)
    
    if resource == None:
        return jsonify({"message": "O resource não existe", "error":True}), 404
    
    db.session.delete(resource)

    try:
        db.session.commit()
        return jsonify({"message": "Resource deletado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel deletar o resource", "error":False}), 200

@app.route("/edit/resource/<int:id>",methods=["PUT"])
def editar_resource(id):
    resource = Resource.query.get(id)
    data = request.get_json()

    if resource == None:
        return jsonify({"message": "O resource não existe", "error":True}), 404
    
    try:
        if "action_id" in data:
            resource.action_id = data["action_id"]
        if "controller_id" in data:
            resource.controller_id = data["controller_id"]

        db.session.commit()
        return jsonify({"message": "Resource editado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar o resource", "error":True}), 200

@app.route("/view/resource/<int:id>",methods=["GET"])
def visualizar_resource(id):
    resource = Resource.query.get(id)

    if resource == None:
        return jsonify({"message": "O resource não existe", "error":True}), 404
    
    return jsonify({
        "data": resource.to_dict(),
        "error": False
    })