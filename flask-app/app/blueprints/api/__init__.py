from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')
 # create api blueprint object and import all routes from this folder
# from . import routes