from app import app, db
from app import Controller
from flask import request, jsonify

@app.route("/list/controller",methods=["GET"])
def listar_controller():
    controllers = Controller.query.all()
    arr = []
    
    for controller in controllers:
        arr.append(controller.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/add/controller",methods=["POST"])
def adicionar_controller():
    data = request.get_json()

    if "name" not in data or data["name"] is None:
        return jsonify ({"Error":True, "Message": "nome não foi informado"}), 400
    
    controller = Controller()
    controller.name = data["name"]
    try:
        db.session.add(controller)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "controller ja existente"})

@app.route("/delete/controller/<int:id>",methods=["DELETE"])
def deletar_controller(id):
    controller = Controller.query.get(id)
    
    if controller == None:
        return jsonify({"message": "O controller não existe", "error":True}), 404
    
    db.session.delete(controller)

    try:
        db.session.commit()
        return jsonify({"message": "Controller deletado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel deletar o controller", "error":False}), 200

@app.route("/edit/controller/<int:id>",methods=["PUT"])
def editar_controller(id):
    controller = Controller.query.get(id)
    data = request.get_json()

    if controller == None:
        return jsonify({"message": "O controller não existe", "error":True}), 404
    
    try:
        if "name" in data:
            controller.name = data["name"]
        db.session.commit()
        return jsonify({"message": "Controller editado com sucesso", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar o controller", "error":True}), 200

@app.route("/view/controller/<int:id>",methods=["GET"])
def visualizar_controller(id):
    controller = Controller.query.get(id)

    if controller == None:
        return jsonify({"message": "O controller não existe", "error":True}), 404
    
    return jsonify({
        "data": controller.to_dict(),
        "error": False
    })