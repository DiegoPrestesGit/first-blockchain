from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")
flask_app_instance = Flask(__name__)

if __name__ == '__main__':
    logger.debug('starting app')
    from api import *
    # flask_app_instance.run(
    #     host="0.0.0.0", port=5000,
    #     debug=True, use_reloader=True
    # )
