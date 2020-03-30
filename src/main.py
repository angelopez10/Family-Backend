"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Family

myFamily = Family ("Doe")

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member', methods=['GET', 'POST'])
@app.route('/member/<int:id>', methods=['GET', 'DELETE', 'PUT'])

def person_group():

    if request.method == 'GET':
        if id is not None:
            member = myFamily.get_member(id)
            if member: 
                return jsonify(member), 200
            else:
                return ({'msg': 'Member Not Found'}), 404
        else:
            members = myFamily.get_all_members()

        return jsonify(members), 200


    if request.method == 'POST':
        member = request.get_json()
        member = myFamily.add_member(member)
        return jsonify(member), 200


    if request.method == 'DELETE':
        myFamily.delete_member(id)
        return jsonify({}), 200

    if request.method == 'PUT':
        member = request.get_json()
        member = myFamily.update_member(id, member)
        return jsonify(member), 200




# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)