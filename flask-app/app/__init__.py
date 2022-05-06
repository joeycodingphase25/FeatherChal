from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# initialize react object APP then import routes to avoid unread errors
from app.blueprints.api import api
app.register_blueprint(api)

from app.blueprints.admin import admin
app.register_blueprint(admin)

from app import routes