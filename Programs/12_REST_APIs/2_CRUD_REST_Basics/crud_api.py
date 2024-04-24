from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

puppies = []  # List of puppy dictionaries


# ? Use Postman to test the API


class PuppyNames(Resource):

    # ? READ
    def get(self, name):

        print("=== In GET ===")

        for pup in puppies:
            if pup["name"] == name:
                print(f"✅ Puppy ({name}) found")
                return pup

        # Puppy not found
        print(f"❌ Puppy ({name}) not found")
        return {"name": None}, 404

    # ? CREATE
    def post(self, name):

        print("=== In POST ===")

        pup = {"name": name}
        puppies.append(pup)
        print(f"✅ Puppy ({name}) added")
        return pup

    # ? DELETE
    def delete(self, name):

        print("=== In DELETE ===")

        for ind, pup in enumerate(puppies):
            if pup["name"] == name:
                deleted_pup = puppies.pop(ind)
                print(f"✅ Puppy ({name}) deleted")
                return {"note": f"delete success (puppy name: {name})"}

        # Puppy not found
        print(f"❌ Puppy ({name}) not found")
        return {"note": "delete failed (puppy name not found)"}


class AllNames(Resource):

    def get(self):
        return {"puppies": puppies}


api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")

if __name__ == '__main__':
    app.run(debug=True)
