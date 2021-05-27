from flask_restful import Api
from app_5000 import flask_app_instance
from .api import api

rest_server = Api(flask_app_instance)
rest_server.add_resource(api, '')
