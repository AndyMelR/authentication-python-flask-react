"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)


@api.route('/signup', methods=['POST'])
def signup():
    password = request.json.get('password', None)
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

@api.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.serialize() for user in User.query.all()]), 200

@api.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get("email")
        password = request.json.get("password")
        user = User.query.filter_by(email=email, password=password).first()
        if User is None:
            return jsonify({"msg":"Bad request, email or password not valid"}), 401
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    except Exception as e:
        return jsonify({"error": e}), 400

@api.route('/private', methods=['GET', 'POST'])
@jwt_required()
def private():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
