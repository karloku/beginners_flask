from flask import request
from app.models import User
from lib import ModelJSONEncoder

class ApplicationController:
    @classmethod
    def index(cls):
        return 'welcome'
