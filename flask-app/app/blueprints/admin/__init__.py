from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

# create blueprint object and import all routes from this folder
from . import routes