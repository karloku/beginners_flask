from app.controllers import *
import inspect

class Router:
    def __init__(self, app):
        self.app = app

    def route(self, rule, func, endpoint=None, **options):
        endpoint = endpoint if endpoint else Router.endpoint(func)
        self.app.add_url_rule(rule, endpoint, func, **options)

    @staticmethod
    def endpoint(func):
        if not inspect.ismethod(func):
            return func.__name__

        controller_name = '.'.join([func.__self__.__module__, func.__self__.__name__])
        return ':'.join([controller_name, func.__name__])

def draw_routes(app):
    router = Router(app)
    router.route('/', ApplicationController.index, methods=['GET'])
    router.route('/users', UsersController.index, methods=['GET'])
    router.route('/users/<user_id>', UsersController.show, methods=['POST'])
