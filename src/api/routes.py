"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def set_signup():
    password = request.json.get('password', 'Andrea')
    email = request.json.get('email', None)
    is_active = request.json.get('is_active', True)
    try:
        new_user = User(password = password, email = email, is_active = is_active)
        db.session.add(new_user)
        db.session.commit()

    except Exception as e:
        print(e)
        return jsonify({'message':f'error: {e}'}), 400

    return jsonify({'message':'ok'}), 200