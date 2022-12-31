from flask import Flask
from flask_restful import Api, Resource
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


api = Api(app)
jwt = JWT(app, authenticate, identity)  # ? creates new endpoint: /auth


puppies = []  # List of puppy dictionaries


class PuppyNames(Resource):

    # ? READ
    def get(self, name):

        for pup in puppies:
            if pup["name"] == name:
                return pup

        return {"name": None}, 404

    # ? CREATE
    def post(self, name):

        pup = {"name": name}
        puppies.append(pup)

        return pup

    # ? DELETE
    def delete(self, name):

        for ind, pup in enumerate(puppies):
            if pup["name"] == name:
                deleted_pup = puppies.pop(ind)
                print(deleted_pup)

                return {"note": f"delete success (puppy name: {name})"}

        return {"note": "delete failed (puppy name not found)"}


class AllNames(Resource):

    # ? Only after authentication can you access this resource
    @jwt_required()
    def get(self):
        return {"puppies": puppies}


api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")

if __name__ == '__main__':
    app.run(debug=True)
