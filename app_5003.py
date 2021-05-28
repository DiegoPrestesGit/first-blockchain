from flask import Flask
import logging as logger
from api.api import app

port = 5003
host = '0.0.0.0'

logger.basicConfig(level="DEBUG")
flask_app_instance = Flask(__name__)

if __name__ == '__main__':
    logger.debug('starting app')
    # from api import *
    app.run(host=host, port=port,
            debug=True, use_reloader=True)
