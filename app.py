from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList
from keys import KEY

app = Flask(__name__)
app.secret_key = KEY
api = Api(app)

jwt = JWT(app, authenticate, identity) #creates new endpoint /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=3000, debug=True)