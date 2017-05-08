from functools import wraps
from flask import make_response, jsonify, request

def json_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers['Content-Type'] != 'application/json':
            response_415 = {'body': {'message': '415 Unsupported Media Type', 'code': 415}}
            return make_response(jsonify(response_415), 415)
        return f(*args, **kwargs)
    return decorated_function
