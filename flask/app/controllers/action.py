from app import app, db
from app import Action
from flask import request, jsonify

@app.route("/list/action",methods=["GET"])
def listar_action():
    actions = Action.query.all()
    arr = []
    
    for action in actions:
        arr.append(action.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/add/action",methods=["POST"])
def adicionar_action():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify ({"Error":True, "Message": "Name não foi informado"}), 400
    
    action = Action()
    action.name = data["name"]
    try:
        db.session.add(action)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "Action ja existente"})

@app.route("/delete/action/<int:id>",methods=["DELETE"])
def deletar_action(id):
    action = Action.query.get(id)
    
    if action == None:
        return jsonify({"message": "O action não existe", "error":True}), 404
    
    db.session.delete(action)

    try:
        db.session.commit()
        return jsonify({"message": "Action deletado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel deletar o action", "error":False}), 200

@app.route("/edit/action/<int:id>",methods=["PUT"])
def editar_action(id):
    action = Action.query.get(id)
    data = request.get_json()

    if action == None:
        return jsonify({"message": "O action não existe", "error":True}), 404
    
    try:
        if "name" in data:
            action.name = data["name"]
        db.session.commit()
        return jsonify({"message": "Action editado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar o action", "error":True}), 200

@app.route("/view/action/<int:id>",methods=["GET"])
def visualizar_action(id):
    action = Action.query.get(id)

    if action == None:
        return jsonify({"message": "O Action não existe", "error":True}), 404
    
    return jsonify({
        "data": action.to_dict(),
        "error": False
    })