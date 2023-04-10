from flask import Blueprint, jsonify, request
from flask_cors import CORS

from models.entities.Chevrolet import Chevrolet
from models.entities.Login import Login
from models.ChevroletModel import ChevroletModel

main = Blueprint('chevrolet_blueprint', __name__)
CORS(main)

@main.route('/')
def get_chevrolet():
    try:
        chevrolet = ChevroletModel.get_data_chevrolet()
        return jsonify(chevrolet)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_chevrolet():
    try:
        requestData = request.json[0];
        web_scrapet_order = requestData['web_scrapet_order']
        web_scrapet_start_url = requestData['web_scrapet_start_url']
        link = requestData['link']
        link_href = requestData['link_href']
        precio = requestData['precio']
        color = requestData['color']
        marca = requestData['marca']       
        modelo = requestData['modelo']
        ano = requestData['ano']
        chevrolet = Chevrolet(web_scrapet_order, web_scrapet_start_url, link, link_href
                                , precio, color, marca, modelo, ano)
        
        print(chevrolet)

        affected_rows = ChevroletModel.add_data_chevrolet(chevrolet)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(chevrolet.web_scrapet_order)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        print("fff")
        print(ex)
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<web_scrapet_order>', methods=['DELETE'])
def delete_chevrolet(web_scrapet_order):
    try:
        chevrolet = Chevrolet(web_scrapet_order)

        affected_rows = ChevroletModel.delete_chevrolet(chevrolet)

        if affected_rows == 1:
            return jsonify(chevrolet.web_scrapet_order)
        else:
            return jsonify({'message': "No chevrolet deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<usuario>/<contrasena>')
def login_chevrolet(usuario, contrasena):
    try:
        movie = ChevroletModel.login_chevrolet(usuario, contrasena)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add-user', methods=['POST'])
def add_user():
    try:
        requestData = request.json[0];
        usuario = requestData['usuario']
        contrasena = requestData['contrasena']
        login = Login(usuario, contrasena)
        
        print(login)

        affected_rows = ChevroletModel.create_user(login)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(login.usuario)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        print("fff")
        print(ex)
        return jsonify({'message': str(ex)}), 500
    
@main.route('/update/<web_scrapet_order>', methods=['PUT'])
def update_chevrolet(web_scrapet_order):
    try:
        requestData = request.json[0];
        precio = requestData['precio']
        color = requestData['color']
        marca = requestData['marca']       
        modelo = requestData['modelo']
        ano = requestData['ano']
        

        affected_rows = ChevroletModel.update_data_chevrolet(precio, color, marca, modelo, ano ,web_scrapet_order)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(web_scrapet_order)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        print("fff")
        print(ex)
        return jsonify({'message': str(ex)}), 500