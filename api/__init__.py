from flask_restful import Api
from app import flask_app_instance
from .blockchain import blockchain

rest_server = Api(flask_app_instance)
rest_server.add_resource(blockchain, '')