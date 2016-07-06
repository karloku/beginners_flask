from flask import request
from app.models import User
from lib import ModelJSONEncoder

class UsersController:
    @classmethod
    def index(cls):
        return ModelJSONEncoder.dumps(User.objects.all().values_list())

    @classmethod
    def show(cls, user_id):
        return ModelJSONEncoder.dumps(User.get_by_id(user_id))
