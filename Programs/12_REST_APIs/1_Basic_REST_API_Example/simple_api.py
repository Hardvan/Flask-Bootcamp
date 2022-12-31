from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)  # ? Used to add resources to the API.


# ? Creating a resource.
class HelloWorld(Resource):

    def get(self):
        return {"data": "Hello, World!"}


# ? Adding the resource to the API.
api.add_resource(HelloWorld, "/")

if __name__ == '__main__':
    app.run(debug=True)
