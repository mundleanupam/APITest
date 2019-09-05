from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from Person import Person
import json

app = Flask(__name__)
api = Api(app)

# user1 = Person("Nicholas", 42, "Network Engineer")
# user2 = Person("Elvin", 32, "Doctor")
# user3 = Person("Jass", 45, "Web Developer")
# users = [user1, user2, user3]

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]


class User(Resource):

    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
            elif (name == 'all'):
                return make_response(jsonify({'users': users}), 200)
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")
app.run(debug=True)
