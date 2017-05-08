from flask import Blueprint, jsonify, request, make_response
from ..models import User
from ..decorators import json_required

auth = Blueprint('auth',__name__)

@auth.route('/ping/')
def ping():
    return jsonify('PONG')

@auth.route('/register/', methods=['POST'])
@json_required
def register():
    res = User.create_from_json(request.json)
    return make_response(jsonify(res['body'])), res['code']
