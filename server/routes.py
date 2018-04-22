from server import app, db
from flask import request, jsonify
from flask_login import current_user, login_user
from models import User


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/register', methods=['GET', 'POST'])
def register():

    json = request.get_json()
    username = json['username']
    password = json['password']
    email = json['email']

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    # print(username)
    # checking if the user already exists
    user = User.query.filter_by(username=username).first()
    user_email = User.query.filter_by(email=email).first()

    if not user and not user_email:
        #print('user doesnt exist.. creating user')

        db.session.add(new_user)
        db.session.commit()
        return jsonify(
            username=new_user.username,
            id=User.query.filter_by(username=username).first().id,
            response_code=200)
    else:
        return jsonify(
            error_message='user already exists',
            response_code=400)


@app.route('/login', methods=['GET', 'POST'])
def login():

    #for login, we get request = {username, password}
    json = request.get_json()

    username = json['username']
    password = json['password']

    # user.id
    # print(json)

    user = User.query.filter_by(username=username).first()
    #print(user)
    if not user:
        return jsonify(error_message='user doesnt exist',
                       response_code=400)
    else:
        if user.check_password(password):
            return jsonify(
                error_message='user logged in ',
                response_code=200)
        else:
            return jsonify(
                error_message='bad password'
            )


