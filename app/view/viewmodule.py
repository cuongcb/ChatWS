from flask import Blueprint, request, jsonify, make_response

import app.constants.constants as constants
import app.constants.params as params

views = Blueprint('register_views', __name__, url_prefix='/views')

from app.control.controlmodule import Control

controller = Control()

@views.route('/login', methods=['POST'])
def login():
    args = request.json

    username = args[USERNAME]
    password = args[PASSWORD]

    if controller.LogInAction(username, password) == True:
        return make_response({'code': constants.SUCCESS, 'message': 'Login passed'}, 200)

    return make_response({'code': constants.FAIL, 'message': 'Login failed'}, 200)

@views.route('/register', methods=['POST'])
def register():
    args = request.json

    username = args[USERNAME]
    password = args[PASSWORD]

    if controller.RegisterAction(username, password) == True:
        return make_response({'code': constants.SUCCESS, 'message': "Register passed"}, 200)

    return make_response({'code': constants.FAIL, 'message': "Register failed"}, 200)
