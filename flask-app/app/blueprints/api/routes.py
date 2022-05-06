import requests
from app.blueprints.api.models import Supervisors, Supervisor
from flask import jsonify
from . import api


# testing the URL return valid JSON response
@api.route('/test', methods=['GET'])
def index():
    response = requests.get("https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers")
    # get response turned into a readable json
    response = response.json()
    # create the Supervisor*s* object with list response
    supervisors = Supervisors(response)
    # grab the list of *Superisor* objects
    super_list = supervisors.listing
    return jsonify([x.to_dict() for x in super_list])
