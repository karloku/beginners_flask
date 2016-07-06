from flask import Flask
from routes import draw_routes

app = Flask(__name__)
draw_routes(app)
