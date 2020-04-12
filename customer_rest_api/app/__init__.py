from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_cors import cross_origin
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
from nameko.standalone.rpc import ClusterRpcProxy


app = Flask(__name__)
api = Api(app)
cors = CORS(app)


app.config.from_object('config')


from .controllers import *