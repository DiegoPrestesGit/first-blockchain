from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse
import requests


class Xescoin:
    def __init__(self):
      