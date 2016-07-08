from flask import request
from app.models import User
from app.serializers import dumps


class UsersController:
    @classmethod
    def index(cls):
        return dumps(User.objects.all())

    @classmethod
    def show(cls, user_id):
        return dumps(User.get_by_id(user_id))
