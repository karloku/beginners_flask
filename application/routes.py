from app.controllers import *

def draw_routes(app):
    app.route("/users")(UsersController.index)
    app.route("/users/<user_id>")(UsersController.show)